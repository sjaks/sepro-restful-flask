from flask_restful import Resource
from flask import request, abort
from common.db import db
from common.authenticate import auth
from models.user import User
import passlib
from passlib import hash
import uuid

class UserResource(Resource):
    def post(self):
        if not request.json:
            abort(415)

        username=request.json['username'],
        password_hash=passlib.hash.sha256_crypt.hash(request.json['password']),
        user = User(username=username, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        
        return {'username': username[0]}
