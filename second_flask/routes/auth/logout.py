from flask import request, jsonify, session
from . import auth_bp


@auth_bp.route('/logout')
def logout():

    user_id = session.get('user_id')

    if user_id:
        session.clear()
        return jsonify({'message': "logged out successfully."})

    else:
        return jsonify({'message': 'Invalid credentials!'})
