from flask import Flask
from flask_restful import Api
from resources.secret import Secret

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = ''

# Define routes
api.add_resource(Secret, '/secrets/<slug>')

if __name__ == '__main__':
    app.run(debug=True)
