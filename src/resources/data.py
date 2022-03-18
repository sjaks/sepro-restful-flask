from flask_restful import Resource
from common.validate import ParamValidator
from common.db import Database

class Data(Resource):
    validator = ParamValidator()
    database = Database()

    @validator.ValidateParam('')
    def get(self):
        return {}
