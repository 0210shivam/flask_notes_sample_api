from flask import Blueprint

notes_bp = Blueprint('notes', __name__)

from . import add_note, all_notes, update_note, delete_note
