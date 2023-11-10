from flask import Blueprint

auth_bp = Blueprint('user', __name__)

from . import register, login, logout, update_profile, delete_profile
