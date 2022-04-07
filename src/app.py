from flask import Flask
from flask_restful import Api
from resources.secret import Secret
from resources.secret import User

app = Flask(__name__)
api = Api(app)

# Define routes
api.add_resource(Secret, '/secrets/<slug>')
api.add_resource(User, '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True)
