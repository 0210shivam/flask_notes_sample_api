from flask import request, jsonify
from second_flask.schemas import user_schema
from . import auth_bp


# Creates Instance of UserSchema -
user_schema = user_schema.UserSchema()


@auth_bp.route('/login', methods=['POST'])
def login():
    # Imports mongo initialize function ->3
    from second_flask.config.db_config import initialize_mongo

    # Initial Step ->
    mongo = initialize_mongo()  # Initialize mongo
    data = request.get_json()
    errors = user_schema.validate(data)

    if errors:
        return jsonify({'message': 'Validation errors', 'errors': errors}), 400

    username = data['username']
    password = data['password']

    user = mongo.db.users.find_one({'username': username})

    if user and password == user['password']:
        # Implement your authentication logic here

        response_data = {
            'message': 'Login successful',
            'user': {
                'username': user['username'],
                'user_id': user['_id'],
                'email': user['email']
            }
        }
        return jsonify(response_data), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
