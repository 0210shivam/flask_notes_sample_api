from second_flask import app
from flask_pymongo import PyMongo
from decouple import config


def initialize_mongo():
    app.config['MONGO_URI'] = config('MONGO_URI')
    mongo = PyMongo(app)
    return mongo
