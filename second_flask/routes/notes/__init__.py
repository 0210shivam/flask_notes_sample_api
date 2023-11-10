from flask import Blueprint

notes_bp = Blueprint('notes', __name__)

from . import add_note
