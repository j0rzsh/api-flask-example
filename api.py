from flask import Blueprint
from flask_restplus import Api, Resource
from logger import Logger

# Init logging
logger = Logger.getLogger(__name__)

blueprint = Blueprint("api", __name__)
api = Api(blueprint)

hello_namespace = api.namespace(
    "hello", description="Create Workmail Service")

# ------------------------ API ------------------------
@hello_namespace.route("")
class Workmail(Resource):

    def __init__(self, api=None):
        self.api = api

    def get(self):
        return {"hello": "world"}
