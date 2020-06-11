from flask import Blueprint
from flask_restful import reqparse, abort, Api, Resource
from flask_restful import fields, marshal_with

from user import Users

user_bp = Blueprint('user', __name__)

user_api = Api(user_bp)

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

@user_api.resource('/login')
class Login(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return 'login'


@user_api.resource('/register')
class Register(Resource):
    def get(self):
        return 'register'


@user_api.resource('/logout')
class Logout(Resource):
    def get(self):
        return 'logout'



