# app/auth.py

from flask_jwt_extended import create_access_token

def generate_jwt_token(user_id):
    # Create JWT token with user ID
    token = create_access_token(identity=user_id)
    return token
