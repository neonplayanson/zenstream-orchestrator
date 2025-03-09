from . import api_namespace_user
from flask_restx import Resource, fields, reqparse
from hashlib import sha256
from app.models.user import User
from flask import make_response


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
        username = args.get("Username")
        password = args.get("Password")
        if type(username) is not str or type(password) is not str:
            return {}, 403
        token = User(username.strip()).login(
            sha256(password.strip().encode()).hexdigest()
        )
        if token:
            response = make_response({}, 202)
            response.headers["TOKEN"] = token

            return response
        return {}, 403
