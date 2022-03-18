from flask import Flask
from flask_restful import Api
from resources.data import Data

app = Flask(__name__)
api = Api(app)

# Define routes
api.add_resource(Data, '/data')

if __name__ == '__main__':
    app.run(debug=True)
