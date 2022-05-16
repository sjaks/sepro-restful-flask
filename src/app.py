from flask import Flask
from flask_restful import Api
from resources.secret import SecretResource
from common.db import db
from models.secret import Secret

app = Flask(__name__)
api = Api(app)

# Flask config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:example@database:5432/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup db
db.app = app
db.init_app(app)
db.create_all()

# Define routes
api.add_resource(SecretResource, '/secrets/<slug>')

if __name__ == '__main__':
    app.run(debug=True)
