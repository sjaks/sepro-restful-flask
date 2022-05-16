from flask_restful import Resource
from common.validate import Validator
from common.db import db
from models.secret import Secret
import uuid

class SecretResource(Resource):
    validator = Validator()

    #@validator.ValidateKey()
    def get(self, slug):
        secret = Secret.query.filter_by(id=str(slug)).first()
        return {'id': str(secret.id), 'slug': secret.slug}

    #@validator.ValidateKey()
    def post(self, slug):
        id = str(uuid.uuid4())
        secret = Secret(id=id, slug=slug)
        db.session.add(secret)
        db.session.commit()
        return {'id': id, 'slug': slug}

    #@validator.ValidateKey()
    def delete(self, slug):
        Secret.query.filter_by(id=str(slug)).delete()
        db.session.commit()
        return {'id': str(slug)}
