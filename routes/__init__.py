from flask import Flask
from .health import health_blueprint

def register_blueprints(app: Flask):
    app.register_blueprint(health_blueprint)