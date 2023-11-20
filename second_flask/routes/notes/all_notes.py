from flask import request, session, jsonify, make_response
from bson import json_util
from . import notes_bp

# TODO - Refactor this ->


@notes_bp.route('/all')
def all_notes():

    user_id = session.get('user_id')

    if user_id:
        from second_flask.config.db_config import initialize_mongo
        mongo = initialize_mongo()
        notes_collection = mongo.db.notes

        # Query MongoDB to find all notes for the given user_id
        notes = notes_collection.find({'user_id': user_id})

        # Convert the MongoDB cursor to a list for easy serialization
        notes_list = json_util.dumps(list(notes))

        # Check if any notes were found
        if not notes_list:
            # Return a response with a 404 status code if no notes were found
            return make_response(jsonify({'message': 'No notes found'}), 404)

        # Return the notes as JSON with a 200 status code
        return notes_list, 200

    else:
        return jsonify({'message': 'Login Required!'}), 401
