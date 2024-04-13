# app/error_handlers.py

from flask_jwt_extended import JWTManager
from flask import jsonify
from app import app

jwt = JWTManager(app)

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({'error': 'Missing Authorization Header'}), 401
