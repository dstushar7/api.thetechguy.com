from app import db
from werkzeug.security import check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=True)
    role_id = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(200), nullable=True)


    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(45), nullable=False, unique=True)