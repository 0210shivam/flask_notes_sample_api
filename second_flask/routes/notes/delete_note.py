from bson import ObjectId
from flask import session, jsonify
from . import notes_bp


@notes_bp.route('/delete/<note_id>', methods=['GET', 'DELETE'])
def delete_note(note_id):

    user_id = session.get('user_id')

    if user_id:
        from second_flask.config.db_config import initialize_mongo
        mongo = initialize_mongo()

        if int(note_id) >= 24:
            note_id = ObjectId(note_id)

            note_id_from_db = mongo.db.notes.find_one({'_id': note_id})

            if str(note_id) == str(note_id_from_db['_id']):
                mongo.db.notes.delete_one({'_id': note_id, 'user_id': user_id})

                return jsonify({'message': 'Deleted Successfully!'})

            else:
                return jsonify({'message': 'No Note found with this id!'})

        else:
            return jsonify({'message': 'Not valid Note Id!'})

    else:
        return jsonify({'message': 'Login Required!'}), 401
