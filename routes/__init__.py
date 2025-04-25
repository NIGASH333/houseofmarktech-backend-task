from flask import Blueprint

# Initialize the routes blueprint
routes_bp = Blueprint('routes', __name__)

# Import the authentication and task routes
from .auth import *
from .tasks import *

# Register the routes with the blueprint
def register_routes(app):
    app.register_blueprint(routes_bp)