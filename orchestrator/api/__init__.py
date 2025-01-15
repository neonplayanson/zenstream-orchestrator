### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

from flask import Blueprint
from flask_restx import Resource, Namespace, reqparse, fields, marshal

from .user import api_namespace_user

api_namespaces = [
    api_namespace_user,
]
