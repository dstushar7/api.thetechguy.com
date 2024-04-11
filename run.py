from flask import jsonify
from app import app

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})


@app.route('/home')
def home():
    return jsonify({"message": "This is the homepage!"})

import app.controller.user_controller as user


if __name__ == '__main__':
    app.run(debug=True)