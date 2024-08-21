from flask import flask
from flask_restful import resource, api, reqparse
from flask mongoengine import Mongoengine

app = flask(__name__)

app.config['MONGODB_SETTINGS'] =[
    'bd': 'users',
    'port': 27017,
    'host': 'mongodb',
    'username': 'admin',
    'passaword': 'admin'
]

_user parser = reqparse.requestParser
_user_parser.add_argument('name')
