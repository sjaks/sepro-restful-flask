from flask import Flask
from flask_restful import Api
from resources.secret import Secret

app = Flask(__name__)
api = Api(app)

# Define routes
api.add_resource(Secret, '/secret/<slug>')

if __name__ == '__main__':
    app.run(debug=True)
