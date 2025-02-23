from . import api_namespace_user
from flask_restx import Resource, reqparse
from app.config import Config
import json


@api_namespace_user.route("user/logout")
class UserLogout(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument(
        "Username", type=str, help="The username.", location="headers"
    )
    get_parser.add_argument("TOKEN", type=str, help="The token.", location="headers")

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.response(200, description="User logged out.")
    @api_namespace_user.response(
        500, description="An error occurred while logging out user."
    )
    def get(self):
        """Logout the user."""
        args = self.get_parser.parse_args()
        username = args.get("Username").strip()
        token = args.get("TOKEN")
        db = Config()._database

        try:
            data = db.execute(
                "SELECT client_tokens FROM users WHERE username = ?",
                (username,),
            )
            data = json.loads(data[0][0])
            data = {k: v for k, v in data.items() if v != token}
            db.execute(
                "UPDATE users SET client_tokens = ? WHERE username = ?",
                (json.dumps(data), username),
            )
            return {}, 200
        except Exception as e:
            return {}, 500
