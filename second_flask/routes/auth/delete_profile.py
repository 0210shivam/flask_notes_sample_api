from bson import ObjectId
from flask import request, jsonify, session
from second_flask.schemas import user_schema
from . import auth_bp


@auth_bp.route('/delete', methods=['DELETE'])
def delete_profile():

    user_id = ObjectId(session.get('user_id'))
    data = request.get_json()

    # get username and password from data object ->
    username = data['username']
    email = data['email']
    password = data['password']

    if user_id:
        from second_flask.config.db_config import initialize_mongo
        mongo = initialize_mongo()

        user = mongo.db.users.find_one({'email': email, 'username': username})

        if user is None:
            return jsonify({'message': 'User not found'}), 404

        if user['password'] == password and ObjectId(user['_id']) == user_id:
            mongo.db.users.delete_one({'_id': user_id})

            session.clear()

            return jsonify({'message': 'Deleted Successfully!'})

    else:
        return jsonify({'message', 'Login required!'})
