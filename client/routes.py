from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import request

from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from hashlib import sha256

from . import app, login_manager, db
#from app.forms import LoginForm, SignupForm
#from app.models import User, MasterClass


@app.get('/')
def index():
    return 'Hello, World!'
