from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import FlaskAppConfig

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db

from . import routes
from api import endpoints
