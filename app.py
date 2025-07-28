from flask import Flask, jsonify

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
