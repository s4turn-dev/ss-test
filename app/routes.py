from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import abort

from flask_login import current_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import login_user
from hashlib import md5

from . import app, login_manager, db
from .forms import LoginForm, SignupForm, RequisitesForm
from models.user import User
from models.requisites import Requisites


# --- General stuff --- 
@app.get('/')
@login_required
def requisitesPage():
    requisites = Requisites.query.filter_by(user_uid=current_user.uid)
    return render_template('requisites.html', user=current_user, requisites=requisites)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def addRequisites():
    form = RequisitesForm()
    if form.validate_on_submit():
        req = Requisites(user_uid=current_user.uid)
        form.populate_obj(req)
        db.session.add(req)
        db.session.commit()
        return redirect(url_for('requisitesPage'))
    return render_template('requisites_form.html', form=form)


@app.route('/edit/<int:req_id>', methods=['GET', 'POST'])
@login_required
def editRequisites(req_id: int):
    try:
        req = Requisites.query.filter_by(user_uid=current_user.uid)[req_id-1]
    except IndexError:
        abort(404)
    else:
        form = RequisitesForm(obj=req)
        if form.validate_on_submit():
            form.populate_obj(req)
            db.session.commit()
            return redirect(url_for('requisitesPage'))
        return render_template('requisites_form.html', form=form)


@app.get('/delete/<int:req_id>')
@login_required
def deleteRequisites(req_id: int):
    try:
        req = Requisites.query.filter_by(user_uid=current_user.uid)[req_id-1]
    except IndexError:
        abort(404)
    else:
        db.session.delete(req)
        db.session.commit()
        return redirect(url_for('requisitesPage'))


@app.get('/activate/<int:req_id>')
@login_required
def activateRequisites(req_id: int):
    try:
        req = Requisites.query.filter_by(user_uid=current_user.uid)[req_id-1]
    except IndexError:
        return 'NOT FOUND'
    else:
        old_active = Requisites.query.filter_by(user_uid=current_user.uid, is_active=True).first()
        if old_active:
            old_active.is_active = False
        req.is_active = True
        db.session.commit()
        return 'OK'



# --- Account management ---
@login_manager.user_loader
def user_loader(uid: int):
    return User.query.get(uid)

@login_manager.unauthorized_handler
def unathorized():
    return redirect(url_for('loginPage'))

def hash_pwd(pwd: str) -> str: return md5(bytes(pwd, 'utf-8')).hexdigest()


@app.get('/login')
def loginPage():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('requisitesPage'))
    return render_template('login.html', form=form)

@app.post('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, password=hash_pwd(form.password.data)).first()
        if user:
            login_user(user)
            return redirect(url_for('requisitesPage'))
        else:
            flash('Wrong credentials')
            return redirect(url_for('loginPage'))
    return redirect(url_for('loginPage'))

@app.get('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('loginPage'))


@app.get('/signup')
def signupPage():
    form = SignupForm()
    if current_user.is_authenticated:
        return redirect(url_for('requisitesPage'))
    return render_template('signup.html', form = SignupForm())

@app.post('/signup')
def signup():
    form = SignupForm()
    if form.is_submitted():
        print('123')
    if form.validate_on_submit():
        username = form.username.data
        password = hash_pwd(form.password.data) 
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('requisitesPage'))
    return render_template('signup.html', form=form)
