from . import api_namespace_user
from flask_restx import Resource, reqparse
from app.models import Invite


@api_namespace_user.route("user/delete_invite")
class UserDeleteInvite(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument("url", type=str, help="The url.", location="headers")

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.response(200, "Deleted an invite.")
    @api_namespace_user.response(500, "Failed to delete an invite.")
    def delete(self):
        """Delete an invite."""
        args = self.get_parser.parse_args()
        url = args.get("url").strip()

        if Invite().delete(url):
            return {}, 200
        return {}, 500
