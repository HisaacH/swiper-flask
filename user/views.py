from flask import Blueprint
from flask_restful import reqparse, abort, Api, Resource

user_bp = Blueprint('user', __name__)

user_api = Api(user_bp)


@user_api.resource('/register')
class Register(Resource):
    def get(self):
        return 'Hello'