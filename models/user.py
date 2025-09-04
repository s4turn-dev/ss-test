from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    requisites = db.relationship('Requisites', backref='user', lazy=True)

    def get_id(self):
        return self.uid

    def __repr__(self):
        return f'User(login={self.login})'
