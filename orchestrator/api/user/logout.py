from . import api_namespace_user
from flask_restx import Resource, reqparse
from app.models.user import User
from utils.wrappers import authenticate


@api_namespace_user.route("user/logout")
class UserLogout(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument(
        "Username", type=str, help="The username.", location="headers"
    )
    get_parser.add_argument("TOKEN", type=str, help="The token.", location="headers")

    @authenticate
    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.response(200, description="User logged out.")
    @api_namespace_user.response(400, description="Invalid credentials.")
    @api_namespace_user.response(
        500, description="An error occurred while logging out user."
    )
    def get(self):
        """Logout the user."""
        args = self.get_parser.parse_args()
        username = args.get("Username")
        token = args.get("TOKEN")
        if type(username) is not str or type(token) is not str:
            return {}, 400

        if User(username).logout(token):
            return {}, 200
        return {}, 500
