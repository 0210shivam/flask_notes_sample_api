from flask import Flask
from flask_session import Session
from .routes.test_db import test_bp
from .routes.auth import auth_bp
from .routes.notes import notes_bp

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set a secret key for the app
app.secret_key = "xyz"

app.register_blueprint(test_bp)  # Test Routes for database
app.register_blueprint(auth_bp, url_prefix='/auth')  # Authentication Routes
app.register_blueprint(notes_bp, url_prefix='/notes')  # Notes Routes
