from . import api_namespace_user
from flask_restx import Resource, fields, reqparse
from app.config import Config
from hashlib import sha256


@api_namespace_user.route("user/register")
class UserRegister(Resource):
    """Resource class for user registration."""

    get_parser = reqparse.RequestParser()
    get_parser.add_argument("Username", type=str, help="The username.", location="args")
    get_parser.add_argument("Password", type=str, help="The password.", location="args")

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.marshal_with(
        {}, description="Registered the user.", code=201
    )
    @api_namespace_user.marshal_with(
        {}, description="Failed to register the user.", code=406
    )
    @api_namespace_user.marshal_with(
        {}, description="An error occurred while registering.", code=500
    )
    def post(self):
        """Register the user."""
        args = self.get_parser.parse_args()
        username = args.get("Username").strip()
        password = sha256(args.get("Password").strip().encode()).hexdigest()
        db = Config()._database
        attempt = db.execute(
            "INSERT INTO users VALUES (?, ?, '{}')", (username, password)
        )
        if type(attempt) is list:
            return {}, 201
        if attempt.sqlite_errorname == "SQLITE_CONSTRAINT_UNIQUE":
            return {}, 409
        return {}, 500
