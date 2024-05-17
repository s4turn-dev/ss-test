from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object(Config)
db = None#SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from . import routes
from api import endpoints
