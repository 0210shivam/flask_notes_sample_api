from flask import Flask
from .routes.test_db import test_bp
from .routes.auth import auth_bp

app = Flask(__name__)

app.register_blueprint(test_bp, url_prefix='/test')  # Test Routes for database
app.register_blueprint(auth_bp, url_prefix='/auth')  # Authentication Routes
