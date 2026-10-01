from flask import Flask
from config import Config
from models import db

app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Import routes
from routes import public_bp
from routes import admin_bp

# Register blueprints
app.register_blueprint(public_bp)
app.register_blueprint(admin_bp)


# Create database automatically if it doesn't exist
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)