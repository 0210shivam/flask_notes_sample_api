from flask import request, jsonify, session
from . import auth_bp


@auth_bp.route('/login', methods=['POST'])
def login():
    # Imports mongo initialize function ->
    from second_flask.config.db_config import initialize_mongo

    # Initial Step ->
    mongo = initialize_mongo()  # Initialize mongo
    data = request.get_json()

    # get username and password from data object ->
    username = data['username']
    email = data['email']
    password = data['password']

    # Check the existence of user ->
    user = mongo.db.users.find_one({'email': email, 'username': username})

    # Check if the username has correct password saved previously ->
    if user and password == user['password']:

        # Assign session for the user who is logged in ->
        session['user_id'] = user['_id']  # object id
        # session_id = request.cookies.get('session')  - Not to do this instead do -
        session_id = session.sid  # With sid for direct access without delay

        response_data = {
            'message': 'Login successful',
            'session_id': session_id,  # sends session id back to user
            'user': {
                'username': user['username'],
                'email': user['email']
            }
        }

        # Do whatever you need - after successful login -
        return jsonify(response_data), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
