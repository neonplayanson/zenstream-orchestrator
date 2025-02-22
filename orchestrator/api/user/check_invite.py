from . import api_namespace_user
from flask_restx import Resource, reqparse
from app.config import Config


@api_namespace_user.route("user/check_invite")
class UserCheckInvite(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument("url", type=str, help="The url.", location="headers")

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.response(202, "Invite is valid.")
    @api_namespace_user.response(403, "Invite is not valid.")
    @api_namespace_user.response(500, "An error occured.")
    def get(self):
        """Check if an invite is valid."""
        db = Config()._database

        args = self.get_parser.parse_args()
        url = args.get("url").strip()
        check = db.execute("SELECT * FROM invites WHERE url = ?", (url,))
        if bool(check):
            return {}, 202
        if type(check) is list:
            return {}, 403
        return {}, 500