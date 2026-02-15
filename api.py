from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'
}

db = MongoEngine(app)
api = Api(app)

class Health(Resource):
    def get(self):
        return {"status": "minha-api-ok"}

api.add_resource(Health, '/health')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
