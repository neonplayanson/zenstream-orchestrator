from . import api_namespace_user
from flask_restx import Resource, fields, reqparse
from app.config import Config


@api_namespace_user.route("user/register")
class UserRegister(Resource):
    """
    Resource class for user registration.
    """

    success_model = api_namespace_user.model(
        "Success",
        {
            "successful": fields.Boolean(
                default=True, description="Is registration successful"
            ),
            "reason": fields.String(
                default=None, description="Null if registration is successful"
            ),
        },
    )
    fail_model = api_namespace_user.model(
        "Fail",
        {
            "successful": fields.Boolean(
                default=False, description="Is registration successful"
            ),
            "reason": fields.String(description="The reason for the failure"),
        },
    )

    get_parser = reqparse.RequestParser()
    get_parser.add_argument("Username", type=str, help="The username.", location="args")
    get_parser.add_argument("Password", type=str, help="The password.", location="args")

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.marshal_with(
        success_model, description="Registered the user.", code=201
    )
    @api_namespace_user.marshal_with(
        fail_model, description="Failed to register the user.", code=406
    )
    def post(self):
        """
        Register the user.

        Parses the request arguments to get the username and password,
        and attempts to insert a new user into the database.

        Returns:
            dict: A dictionary containing the registration status and reason.
            int: The HTTP status code.
        """
        args = self.get_parser.parse_args()
        username = args.get("Username")
        password = args.get("Password")
        db = Config()._database
        attempt = db.execute(
            "INSERT INTO users VALUES (?, ?, '{}')", (username, password)
        )
        if type(attempt) is list:
            return {"successful": True, "reason": None}, 201
        else:
            if attempt.sqlite_errorname == "SQLITE_CONSTRAINT_UNIQUE":
                return {
                    "successful": False,
                    "reason": "Username is already taken.",
                }, 406
            else:
                return {"successful": False, "reason": "Unknown error."}, 406
