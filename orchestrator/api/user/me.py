### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

import random
from flask_restx import Resource, fields, reqparse
from utils.wrappers import authenticate
from . import api_namespace_user


@api_namespace_user.route("user/me")
class UserAuthenticate(Resource):
    get_model = api_namespace_user.model(
        "Get",
        {
            "authorized": fields.Boolean(description="Is user authorized"),
        },
    )
    get_parser = reqparse.RequestParser()
    get_parser.add_argument("UserId", type=str, help="The user ID.", location="args")

    @authenticate
    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.marshal_with(get_model, description="Get the user's profile.")
    def get(self):
        """Get the user's profile."""
        args = self.get_parser.parse_args()

        user_id = args.get("UserId")

        is_authorized = random.choice([True, False])
        return {"UserId": user_id, "authorized": is_authorized}
