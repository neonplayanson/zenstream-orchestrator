### ======================================================================
### ZenStream Orchestrator
### Copyright 2019-2024 © Rystal. All Rights Reserved.
### ======================================================================

import os
import importlib
from .user import api_namespace_user

api_namespaces = [
    api_namespace_user,
]

endpoints = os.path.join(os.path.dirname(__file__))


def list_folders(directory):
    return [
        name
        for name in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, name))
    ]


for endpoint in list_folders(endpoints):
    endpoint_path = os.path.join(endpoints, endpoint)
    for method in os.listdir(endpoint_path):
        if method.endswith(".py") and method != "__init__.py":
            module_name = f"api.{endpoint}.{method[:-3]}"
            importlib.import_module(module_name)
