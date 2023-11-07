from flask import request
from . import test_bp


@test_bp.route('/')
def hello():
    return "hello"


# Add one document
@test_bp.route('/add_one', methods=['POST'])
def adding():
    from second_flask.config.db_config import initialize_mongo

    data = request.get_json()
    mongo = initialize_mongo()
    mongo.db.users.insert_one(data)
    return "Success"


# Add many Document
@test_bp.route('/add_many', methods=['POST'])
def adds():
    from second_flask.config.db_config import initialize_mongo

    data = request.get_json()
    mongo = initialize_mongo()
    mongo.db.users.insert_many(data)
    return "Success"
