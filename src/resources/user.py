from flask_restful import Resource
from common.validate import Validator
from common.db import Database

class User(Resource):
    validator = Validator()
    database = Database()

    #@validator.ValidateKey()
    #@validator.ValidateBody()
    def post(self, slug):
        return {"method": "post"}

    #@validator.ValidateKey()
    def delete(self, slug):
        return {"method": "delete"}
