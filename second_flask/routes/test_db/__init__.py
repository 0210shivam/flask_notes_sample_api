from flask import Blueprint

test_bp = Blueprint('test', __name__)

from . import test_db
