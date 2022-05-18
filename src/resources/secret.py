from flask_restful import Resource
from flask import abort
from common.db import db
from common.authenticate import auth
from models.secret import Secret
import uuid

class SecretResource(Resource):
    @auth.login_required
    def get(self, slug):
        username = auth.username()
        secret = Secret.query.filter_by(id=str(slug)).first()

        if username != secret.user:
            abort(401)

        return {'id': str(secret.id), 'slug': secret.slug, 'user': username}

    @auth.login_required
    def post(self, slug):
        id = str(uuid.uuid4())
        username = auth.username()
        secret = Secret(id=id, slug=slug, user=username)
        db.session.add(secret)
        db.session.commit()
        return {'id': id, 'slug': slug, 'user': username}

    @auth.login_required
    def delete(self, slug):
        username = auth.username()
        secret = Secret.query.filter_by(id=str(slug)).first()

        if username != secret.user:
            abort(401)

        Secret.query.filter_by(id=str(slug)).delete()
        db.session.commit()
        return {'id': str(slug), 'user': username}
