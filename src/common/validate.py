from flask import request
from werkzeug.exceptions import BadRequest

class Validator():
    def ValidateParam(self, param):
        def inner(f):
            def validate(self, *args):
                args = request.args

                if not param in args:
                    raise BadRequest(f"missing '{param}' in params")

                return f(self)
            return validate
        return inner

    def ValidateKey(self, key):
        return

    def ValidateBody(self, body):
        return
