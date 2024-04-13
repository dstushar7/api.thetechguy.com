# app/controllers/user_controller.py

from flask import jsonify, request, session
from app import app
from app.service.user_service import UserService
from app.service.auth_service import AuthService
from app.auth.auth import role_required
from flask_jwt_extended import jwt_required

auth_service = AuthService()


@app.route('/register', methods=['POST'])
def register():
    # Parse request data
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role_id = data.get('role_id')  # Retrieve the role from the request data

    # Validate input data
    if not username or not email or not password or not role_id:
        return jsonify({'error': 'Please provide username, role, email, and password'}), 400

    # Register user using the UserService
    return UserService.register_user(username, email, password, role_id)


@app.route('/login', methods=['POST'])
def login():
    # Parse login credentials from request
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Authenticate user
    user = auth_service.authenticate_user(username, password)
    if user:
        # Generate JWT token for the authenticated user
        token = auth_service.generate_jwt_token(user.id)

        # Create session for the user
        session['user_id'] = user.id
        session.permanent = True  # Set session to be permanent (e.g., valid for 1 day)
        
        return jsonify({'token': token, 'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
    

@app.route('/admin/dashboard')
@jwt_required()
@role_required('Admin')
def admin_dashboard():
    # Only admin users can access this route
    return jsonify({'message': 'Welcome to the admin dashboard'})

@app.route('/visitor/home')
@jwt_required()
@role_required('Visitor','Admin')
def visitor_home():
    # Only visitor users can access this route
    return jsonify({'message': 'Welcome to the user home page'})