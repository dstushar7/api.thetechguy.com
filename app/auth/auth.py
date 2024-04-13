# app/auth.py

from flask_jwt_extended import create_access_token
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from app.model.user_model import User, UserRole
from flask import jsonify

def generate_jwt_token(user_id):
    # Create JWT token with user ID
    token = create_access_token(identity=user_id)
    return token

def role_required(*role_names):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get the current user's ID from the JWT token
            current_user_id = get_jwt_identity()
            # Retrieve the user from the database
            user = User.query.get(current_user_id)
            # Retrieve the user's role from the database
            user_role = UserRole.query.get(user.role_id)

            # Check if the user has any of the required roles
            if user_role.role_name in role_names:
                # User has one of the required roles, execute the decorated function
                return func(*args, **kwargs)
            
            # User does not have any of the required roles, return an error response
            return jsonify({'error': 'Permission denied'}), 403
        return wrapper
    return decorator