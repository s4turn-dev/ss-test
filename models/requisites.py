from . import db

class Requisites(db.Model):
    __tablename__ = 'requisites'
    uid = db.Column(db.Integer, primary_key=True)
    user_uid = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)

    bic = db.Column(db.String(9), nullable=False)
    bank = db.Column(db.String(32), nullable=False)
    checking_account = db.Column(db.String(32), nullable=False)
    correspondent_account = db.Column(db.String(32), nullable=False)
    swift = db.Column(db.String(32), nullable=False)
    iban = db.Column(db.String(32), nullable=True)

    is_active = db.Column(db.Boolean, nullable=False, default=False)

