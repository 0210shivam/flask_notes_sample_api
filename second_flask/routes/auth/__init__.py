from flask import Blueprint

auth_bp = Blueprint('user', __name__)

from . import login, register
