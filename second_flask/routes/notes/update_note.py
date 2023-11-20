import struct

from bson import ObjectId
from flask import request, session, jsonify
from second_flask.schemas import notes_schema
from . import notes_bp

notes_schema = notes_schema.NotesSchema()


@notes_bp.route('/update/<note_id>', methods=['GET', 'PATCH'])
def update_note(note_id):

    user_id = session.get('user_id')

    if user_id:

        if len(note_id) >= 24:
            # Convert note id into object id ->
            note_id = ObjectId(note_id)

            from second_flask.config.db_config import initialize_mongo
            mongo = initialize_mongo()
            data = request.get_json()
            errors = notes_schema.validate(data)  # Validate input by deserializing it

            # Show message if there is any error ->
            if errors:
                return jsonify({'message': 'Validation errors', 'errors': errors}), 400  # Returns error message

            # Get title and description from data ->
            title = data['title']
            desc = data['desc']

            note_id_from_db = mongo.db.notes.find_one({'_id': note_id})

            # All clear then -
            if str(note_id) == str(note_id_from_db['_id']):
                update_note_data = {'$set': {'title': title, 'desc': desc}}
                mongo.db.notes.update_one({'_id': note_id, 'user_id': user_id}, update_note_data)
                # TODO - Here timestamp will not be updated.

                return jsonify('message', "Updated Successfully!"), 200

            else:
                return jsonify({'message': 'No Note found with this id!'})

        else:
            return jsonify({'message': 'Not valid Note Id!'})

    else:
        return jsonify({'message': 'Login Required!'}), 401
