# Flask Task API

This project is a REST API built using Python Flask that allows users to register, log in, and manage their tasks. The API supports user-specific task management, including adding, viewing, and deleting tasks. It uses simple token/session logic for authentication and stores data in a JSON file.

## Features

- User registration and login
- User-specific task management (add, view, delete tasks)
- Simple token/session authentication
- File-based data handling using JSON

## Project Structure

```
flask-task-api
├── app.py               # Entry point of the application
├── models.py            # Data models for users and tasks
├── routes               # Contains route definitions
│   ├── __init__.py      # Initializes the routes package
│   ├── auth.py          # User authentication routes
│   └── tasks.py         # Task management routes
├── data                 # Data storage
│   └── users_tasks.json  # JSON file for user and task data
├── utils                # Utility functions
│   ├── __init__.py      # Initializes the utils package
│   └── auth_utils.py     # Authentication utility functions
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-task-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. The API will be available at `http://localhost:5000`.

## API Endpoints

### Authentication

- **POST /register**: Register a new user
- **POST /login**: Log in an existing user

### Tasks

- **POST /tasks**: Add a new task
- **GET /tasks**: View all tasks for the logged-in user
- **DELETE /tasks/<task_id>**: Delete a specific task

## Usage Examples

You can interact with the API using tools like **curl** or **Postman**.

### Register a User

**Endpoint:** `POST /auth/register`  
**Example with curl:**
```sh
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"testuser\",\"password\":\"testpass\"}"
```

### Login

**Endpoint:** `POST /auth/login`  
**Example with curl:**
```sh
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"testuser\",\"password\":\"testpass\"}"
```
**Response:**  
```json
{"token": "your_jwt_token_here"}
```

### Add a Task

**Endpoint:** `POST /tasks/tasks`  
**Example with curl:**
```sh
curl -X POST http://localhost:5000/tasks/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: your_jwt_token_here" \
  -d "{\"content\":\"My first task\"}"
```

### View Tasks

**Endpoint:** `GET /tasks/tasks`  
**Example with curl:**
```sh
curl -X GET http://localhost:5000/tasks/tasks \
  -H "Authorization: your_jwt_token_here"
```

### Delete a Task

**Endpoint:** `DELETE /tasks/tasks/<task_id>`  
**Example with curl:**
```sh
curl -X DELETE http://localhost:5000/tasks/tasks/1 \
  -H "Authorization: your_jwt_token_here"
```

---

**Note:**  
- Replace `your_jwt_token_here` with the token you receive from the login endpoint.
- You can use similar requests in Postman by setting the method, URL, headers, and body as shown above.

## License

This project is licensed under the MIT License.
