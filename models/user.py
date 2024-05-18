from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True)
    password = db.Column(db.String(32), index=True)

    def get_id(self):
        return self.uid

    def __repr__(self):
        return f'User(login={self.login})'
