from flask import request, session, jsonify
from second_flask.models.Note import Notes
from second_flask.schemas import notes_schema
from . import notes_bp

notes_schema = notes_schema.NotesSchema()


@notes_bp.route('/add', methods=['POST'])
def add_note():

    from second_flask.config.db_config import initialize_mongo

    # If logged-in then get the user_id from session ->
    user_id = session.get('user_id')

    if user_id:

        # Initial Step ->
        mongo = initialize_mongo()  # Initialize mongo
        data = request.get_json()  # Get data from request's body - title, desc
        errors = notes_schema.validate(data)  # Validate input by deserializing it

        # Show message if there is any error ->
        if errors:
            return jsonify({'message': 'Validation errors', 'errors': errors}), 400  # Returns error message

        # Get title and description from data ->
        title = data['title']
        desc = data['desc']

        # All clear then -
        new_note = Notes(user_id, title, desc)

        mongo.db.notes.insert_one(
            {
                'user_id': new_note.user_id,
                'title': new_note.title,
                'desc': new_note.desc,
                'timestamp': new_note.timestamp
            }
        )

        return jsonify({'message': 'Note added successfully'}), 201

    # Return message if user is not logged-in ->
    else:
        return jsonify({'message': 'Log in required!'})
