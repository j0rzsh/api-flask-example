from flask import Blueprint
from flask_restx import Api, Resource

blueprint = Blueprint("api", __name__)
api = Api(blueprint)

hello_namespace = api.namespace(
    "hello", description="Example")

# ------------------------ API ------------------------
@hello_namespace.route("")
class Example(Resource):

    def __init__(self, api=None):
        self.api = api

    def get(self):
        return {"hello": "world"}
