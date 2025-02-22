from . import api_namespace_user
from flask_restx import Resource, fields, reqparse
from flask import make_response
from app.config import Config
from hashlib import sha256
from app.modules.token import Token
from datetime import datetime, timedelta
import json


@api_namespace_user.route("user/login")
class UserLogin(Resource):
    response_model = api_namespace_user.model(
        "Response",
        {
            "successful": fields.Boolean(description="Is login successful"),
            "reason": fields.String(description="The reason for the failure"),
        },
    )

    get_parser = reqparse.RequestParser()
    get_parser.add_argument(
        "Username", type=str, help="The username.", location="headers"
    )
    get_parser.add_argument(
        "Password", type=str, help="The password.", location="headers"
    )

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.response(202, "Login the user.")
    @api_namespace_user.response(403, "Failed to login the user.")
    @api_namespace_user.response(500, "An error occurred while logging in.")
    def post(self):
        """Login the user."""
        args = self.get_parser.parse_args()
        username = args.get("Username").strip()
        password = sha256(args.get("Password").strip().encode()).hexdigest()
        db = Config()._database

        data = db.execute(
            "SELECT client_tokens FROM users WHERE username = ?",
            (username,),
        )
        data = json.loads(data[0][0])
        for key in data:
            if datetime.strptime(key, "%Y-%m-%d %H:%M:%S.%f") < datetime.now():
                del data[key]
        db.execute(
            "UPDATE users SET client_tokens = ? WHERE username = ?",
            (json.dumps(data), username),
        )

        check = db.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        if check:
            token = Token.generate_token()

            data = db.execute(
                "SELECT client_tokens FROM users WHERE username = ?",
                (username,),
            )
            data = json.loads(data[0][0])
            data[str(datetime.now() + timedelta(days=7))] = token
            db.execute(
                "UPDATE users SET client_tokens = ? WHERE username = ?",
                (json.dumps(data), username),
            )

            response = make_response({}, 202)
            response.headers["TOKEN"] = token

            return response
        if type(check) is list:
            return {}, 403
        return {}, 500
