from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World from Render!"

@app.route('/json')
def return_json():
    return jsonify(message="Hello, JSON World!", status="success")

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name.capitalize()}! Welcome to the Flask App."

@app.route('/health')
def health():
    return "OK", 200

# ✅ POST method route
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify(message=f"Hello, {name}! Your data was received."), 200
