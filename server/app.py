from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import db and models
from models import db, User, Lawyer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:apple@localhost:5432/lawyerup'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import Blueprints for APIs
from api.users import users_bp
from api.lawyers import lawyers_bp

# Register Blueprints
app.register_blueprint(users_bp)
app.register_blueprint(lawyers_bp)

if __name__ == '__main__':
    app.run(debug=True)
