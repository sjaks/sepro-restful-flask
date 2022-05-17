from flask_restful import Resource
from common.db import db
from common.authenticate import auth
from models.secret import Secret
import uuid

class SecretResource(Resource):
    @auth.login_required
    def get(self, slug):
        secret = Secret.query.filter_by(id=str(slug)).first()
        return {'id': str(secret.id), 'slug': secret.slug}

    @auth.login_required
    def post(self, slug):
        id = str(uuid.uuid4())
        secret = Secret(id=id, slug=slug)
        db.session.add(secret)
        db.session.commit()
        return {'id': id, 'slug': slug}

    @auth.login_required
    def delete(self, slug):
        Secret.query.filter_by(id=str(slug)).delete()
        db.session.commit()
        return {'id': str(slug)}
