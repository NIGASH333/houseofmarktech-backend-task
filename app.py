from flask import Flask
from routes.auth import auth_bp
from routes.tasks import tasks_bp
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
# Load data from JSON file


data_file = 'data/users_tasks.json'

if not os.path.exists(data_file):
    with open(data_file, 'w') as f:
        json.dump({"users": [], "tasks": []}, f)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(tasks_bp, url_prefix='/tasks')

@app.route('/')
def home():
    return "Flask Task API is running!"

if __name__ == '__main__':
    app.run(debug=True)