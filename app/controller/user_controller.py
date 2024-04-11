# app/controllers/user_controller.py

from flask import jsonify
from app import app

@app.route('/users')
def get_users():
    # Sample data
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"},
        {"id": 3, "name": "Bob"}
    ]
    return jsonify(users)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    # Sample data
    users = {
        1: {"id": 1, "name": "John"},
        2: {"id": 2, "name": "Alice"},
        3: {"id": 3, "name": "Bob"}
    }
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
