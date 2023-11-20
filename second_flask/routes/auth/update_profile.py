from bson import ObjectId
from flask import request, jsonify, session
from second_flask.schemas import user_schema
from . import auth_bp

# Creates Instance of UserSchema -
user_schema = user_schema.UserSchema()


@auth_bp.route('/update', methods=['PATCH'])
def update_profile():

    user_id = ObjectId(session.get('user_id'))

    if user_id:
        from second_flask.config.db_config import initialize_mongo
        mongo = initialize_mongo()  # Initialize mongo
        data = request.get_json()

        # get username and password from data object to be updated ->
        username = data['username']
        email = data['email']
        password = data['password']

        # Validate upcoming Credentials ->
        errors = user_schema.validate(data)  # Validate input by deserializing it

        if errors:
            return jsonify({'message': 'Validation errors', 'errors': errors}), 400  # Returns error message

        # Actual user ->
        user = mongo.db.users.find_one({'_id': user_id})

        if user is None:
            return jsonify({'message': 'User not found'}), 404

        if user['password'] == password:

            # Check if another user with this email exists ->
            existing_user = mongo.db.users.find_one({'email': email})

            if not existing_user:
                update_data = {'$set': {'email': email, 'username': username}}
                mongo.db.users.update_one({'_id': user_id}, update_data)

                return jsonify({'message': 'Details updated Successfully'}), 200

            else:
                return jsonify({'message': 'User with this email, already exists.'})

        else:
            return jsonify({'message': 'Wrong Password!'})

    else:
        return jsonify({'message': 'Login required!'})
