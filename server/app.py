import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Import db and models
from models import db

# Create the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:apple@localhost:5432/lawyerup'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Load secret key from environment
SECRET_KEY = os.getenv("ACCESS_TOKEN_SECRET")

# Enable CORS and specify allowed origins, headers, and methods
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True, allow_headers=["Content-Type", "Authorization"], methods=["GET", "POST","PUT", "OPTIONS"])

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import Blueprints for APIs
from api.users import users_bp
from api.lawyers import lawyers_bp
from api.services import services_bp
from api.booking import bookings_bp

# Register Blueprints
app.register_blueprint(users_bp, url_prefix='/api')
app.register_blueprint(lawyers_bp, url_prefix='/api')
app.register_blueprint(services_bp, url_prefix='/api')
app.register_blueprint(bookings_bp, url_prefix='/api')
if __name__ == '__main__':
    app.run(debug=True)
