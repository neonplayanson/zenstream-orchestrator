from . import api_namespace_user
from flask_restx import Resource, fields, reqparse
from app.config import Config


@api_namespace_user.route("user/authenticate")
class AuthenticateUser(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument(
        "Username", type=str, help="The username.", location="headers"
    )
    get_parser.add_argument(
        "TOKEN", type=str, help="The token.", location="headers"
    )

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.response(201, description="User authenticated.")
    @api_namespace_user.response(403, description="User unauthenticated.")
    @api_namespace_user.response(500, description="An error occurred while authenticating.")
    def get(self):
        args = self.get_parser.parse_args()
        username = args.get("Username").strip()
        token = args.get("TOKEN").strip()
        db = Config()._database
        check = db.execute(
            "SELECT * FROM users WHERE username = ? AND client_tokens LIKE ?",
            (username, f"%{token}%"),
        )
        if bool(check):
            return {}, 201
        if type(check) is list:
            return {}, 403
        return {}, 500