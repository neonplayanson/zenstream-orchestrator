### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

from flask_restx import Resource, Namespace, reqparse, fields, marshal

api_namespace_user_authenticate = Namespace(
    "Authenticate", description="User authentication"
)
