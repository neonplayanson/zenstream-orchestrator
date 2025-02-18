from . import api_namespace_user
from flask_restx import Resource, fields, reqparse
from flask import make_response
from app.config import Config
from hashlib import sha256
from app.modules.token import Token


@api_namespace_user.route("user/login")
class UserLogin(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument(
        "Username", type=str, help="The username.", location="headers"
    )
    get_parser.add_argument(
        "Password", type=str, help="The password.", location="headers"
    )

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.marshal_with({}, description="Login the user.", code=201)
    @api_namespace_user.marshal_with({}, description="Failed to login the user.", code=403)
    @api_namespace_user.marshal_with({}, description="An error occurred while logging in.", code=500)
    def post(self):
        """Login the user."""
        args = self.get_parser.parse_args()
        username = args.get("Username").strip()
        password = sha256(args.get("Password").strip().encode()).hexdigest()
        db = Config()._database
        check = db.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        if bool(check):
            response = make_response({}, 201)
            response.headers["TOKEN"] = Token.generate_token()
            return response
        if type(check) is list:
            return {}, 403
        return {}, 500
