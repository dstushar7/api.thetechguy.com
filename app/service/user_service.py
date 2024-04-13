# app/services/user_service.py

from app.model.user_model import User
from app import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

class UserService:
    @staticmethod
    def register_user(username, email, password, role):
        if User.query.filter_by(username=username).first() is not None:
            return {'error': 'Username already exists'}, 409
        if User.query.filter_by(email=email).first() is not None:
            return {'error': 'Email already exists'}, 409
        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create a new user object
        new_user = User(username=username, email=email, password=hashed_password, role_id=role)

        # Add the new user to the database
        try:
            db.session.add(new_user)
            db.session.commit()
            return {'message': 'User registered successfully'}, 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
