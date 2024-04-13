# app/service/auth_service.py

from app.auth.auth import generate_jwt_token
from app.model.user_model import User

class AuthService:
    def authenticate_user(self, username, password):
        # Authenticate user logic (replace with your own)
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user
        else:
            return None

    def generate_jwt_token(self, user_id):
        # Generate JWT token for the user
        return generate_jwt_token(user_id)
