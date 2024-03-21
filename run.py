from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})


@app.route('/home')
def home():
    return jsonify({"message": "This is the homepage!"})

if __name__ == '__main__':
    app.run(debug=True)
