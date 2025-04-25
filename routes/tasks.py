from flask import Blueprint, request, jsonify, g
import json
import os
from functools import wraps
from utils.auth_utils import decode_token

tasks_bp = Blueprint('tasks', __name__)
DATA_FILE = os.path.join('data', 'users_tasks.json')

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401
        user_id = decode_token(token)
        if not user_id:
            return jsonify({'error': 'Invalid or expired token!'}), 401
        g.user = {'id': user_id}
        return f(*args, **kwargs)
    return decorated

@tasks_bp.route('/')
def tasks_root():
    return "Tasks API Root"

@tasks_bp.route('/tasks', methods=['POST'])
@token_required
def add_task():
    data = load_data()
    user_id = g.user['id']
    task_content = request.json.get('content')
    
    if not task_content:
        return jsonify({'error': 'Task content is required'}), 400
    
    task_id = len(data.get(user_id, [])) + 1
    task = {'id': task_id, 'content': task_content}
    
    if user_id not in data:
        data[user_id] = []
    data[user_id].append(task)
    
    save_data(data)
    return jsonify(task), 201

@tasks_bp.route('/tasks', methods=['GET'])
@token_required
def view_tasks():
    data = load_data()
    user_id = g.user['id']
    
    tasks = data.get(user_id, [])
    return jsonify(tasks), 200

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(task_id):
    data = load_data()
    user_id = g.user['id']
    user_tasks = data.get(user_id, [])
    new_tasks = [task for task in user_tasks if task['id'] != task_id]
    if len(user_tasks) == len(new_tasks):
        return jsonify({'error': 'Task not found'}), 404
    data[user_id] = new_tasks
    save_data(data)
    return jsonify({'message': 'Task deleted successfully'}), 200