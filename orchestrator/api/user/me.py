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
    get_parser.add_argument("token", type=str, help="The auth token.", location="args")

    @authenticate
    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.marshal_with(
        get_model, description="Check if the user is authorized"
    )
    def get(self):
        """Check if the user is authorized."""
        args = self.get_parser.parse_args()
        is_authorized = random.choice([True, False])
        return {"authorized": is_authorized}
