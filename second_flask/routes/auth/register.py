from flask import request, jsonify
from second_flask.models.User import User
from second_flask.schemas import user_schema
from . import auth_bp


# Creates Instance of UserSchema -
user_schema = user_schema.UserSchema()


# Endpoint to register valid user -
@auth_bp.route('/register', methods=['POST'])
def register():
    # Imports mongo initialize function ->
    from second_flask.config.db_config import initialize_mongo

    # Initial Step ->
    mongo = initialize_mongo()  # Initialize mongo
    data = request.get_json()  # Get data from request's body
    errors = user_schema.validate(data)  # Validate input by deserialize it

    if errors:
        return jsonify({'message': 'Validation errors', 'errors': errors}), 400  # Returns error message

    # Proceed further on model's parameters, if validation succeed ->
    username = data['username']
    email = data['email']
    password = data['password']

    # Check for existence of user ->
    existing_user = mongo.db.users.find_one({'username': username})
    if existing_user:
        return jsonify({'message': 'User already exists'}), 400

    # All Clear, Creates user instance with provided fields ->
    new_user = User(username, email, password)

    mongo.db.users.insert_one(
        {
            'username': new_user.username,
            'email': new_user.email,
            'password': new_user.password
        }
    )
    return jsonify({'message': 'User registered successfully'}), 201
