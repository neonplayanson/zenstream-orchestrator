from . import api_namespace_user
from flask_restx import Resource, reqparse
from app.config import Config
from datetime import datetime
import json


@api_namespace_user.route("user/authenticate")
class AuthenticateUser(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument(
        "Username", type=str, help="The username.", location="headers"
    )
    get_parser.add_argument("TOKEN", type=str, help="The token.", location="headers")

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.response(202, description="User authenticated.")
    @api_namespace_user.response(403, description="User unauthenticated.")
    @api_namespace_user.response(
        500, description="An error occurred while authenticating."
    )
    def post(self):
        """Authenticate the user."""
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
        except Exception as e:
            return {}, 403
        for key in data:
            if datetime.strptime(key, "%Y-%m-%d %H:%M:%S.%f") < datetime.now():
                del data[key]
        db.execute(
            "UPDATE users SET client_tokens = ? WHERE username = ?",
            (json.dumps(data), username),
        )

        check = db.execute(
            "SELECT * FROM users WHERE username = ? AND client_tokens LIKE ?",
            (username, f"%{token}%"),
        )
        if bool(check):
            return {}, 202
        if type(check) is list:
            return {}, 403
        return {}, 500
