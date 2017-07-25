"""End point definition."""
from flask import Blueprint
from flask_restful import Api

# local imports
from app.views import AuthRegister, AuthLogin, BucketlistView, ItemView
# initialize api blueprint
api_blueprint = Blueprint('api', __name__)
# # initialize the api class
api = Api(api_blueprint)

api.add_resource(AuthRegister, '/auth/register')
api.add_resource(AuthLogin, '/auth/login')
