from . import api_namespace_user
from flask_restx import Resource, reqparse
from app.config import Config
from random import choice
from string import ascii_letters, digits


@api_namespace_user.route("user/generate_invite")
class UserGenerateInvite(Resource):
    get_parser = reqparse.RequestParser()

    @api_namespace_user.doc(parser=get_parser)
    @api_namespace_user.response(201, "Generate an invite.")
    @api_namespace_user.response(500, "Failed to generate an invite.")
    def post(self):
        """Generate an invite."""
        db = Config()._database

        url = "".join(choice(ascii_letters + digits) for _ in range(64))
        exec = db.execute("INSERT INTO invites VALUES (?)", (url,))

        if type(exec) is list:
            return {"url": url}, 201

        return {}, 500
