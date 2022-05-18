from flask_restful import Resource
from flask import request, abort
from common.db import db
from common.authenticate import auth
from models.user import User
import passlib
from passlib import hash
import uuid

class UserResource(Resource):
    # Register new user
    def post(self):
        if not request.json:
            abort(415, 'username and password required')

        username = request.json['username']
        password = request.json['password']

        # More password strenght meters should be implemented here
        if len(password) < 16:
            abort(403, 'password too weak')

        password_hash = passlib.hash.sha256_crypt.hash(password)
        user = User(username=username, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        
        return {'username': username}
