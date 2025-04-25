from flask import Blueprint, request, jsonify
import json
import os
from utils.auth_utils import generate_token, validate_token

auth_bp = Blueprint('auth', __name__)

data_file = os.path.join('data', 'users_tasks.json')

def load_data():
    if not os.path.exists(data_file):
        return {"users": {}, "tasks": {}}
    with open(data_file, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f)

@auth_bp.route('/')
def auth_root():
    return "Auth API Root"

@auth_bp.route('/register', methods=['POST'])
def register():
    data = load_data()
    username = request.json.get('username')
    password = request.json.get('password')

    if username in data['users']:
        return jsonify({"message": "User already exists"}), 400

    data['users'][username] = password
    save_data(data)
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = load_data()
    username = request.json.get('username')
    password = request.json.get('password')

    if username not in data['users'] or data['users'][username] != password:
        return jsonify({"message": "Invalid credentials"}), 401

    token = generate_token(username)
    return jsonify({"token": token}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    if not validate_token(token):
        return jsonify({"message": "Invalid token"}), 401

    return jsonify({"message": "Logged out successfully"}), 200