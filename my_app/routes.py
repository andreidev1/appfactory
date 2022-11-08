
from functools import wraps

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restx import Api, Resource, fields, marshal_with
from . import db
from . import create_app as app

migrate = Migrate(app, db) 



api = Api(app)




userFields = {
    'admin' : fields.String,
    'id' : fields.Integer,
    'public_id' : fields.String,
    'name' : fields.String,
    'password' : fields.String
}



class Users(Resource):
    @marshal_with(userFields)

    def get(self):

        users = User.query.all()

        return users

api.add_resource(Users, '/users')