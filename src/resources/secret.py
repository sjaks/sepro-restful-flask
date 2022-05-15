from flask_restful import Resource
from common.validate import Validator
from common.db import Database

class Secret(Resource):
    validator = Validator()
    database = Database()

    #@validator.ValidateKey()
    @validator.ValidateParam('field')
    def get(self, slug):
        return {"method": "get"}

    #@validator.ValidateKey()
    #@validator.ValidateBody()
    def post(self, slug):
        return {"method": "post"}

    #@validator.ValidateKey()
    #@validator.ValidateBody()
    def put(self, slug):
        return {"method": "put"}

    #@validator.ValidateKey()
    def delete(self, slug):
        return {"method": "delete"}
