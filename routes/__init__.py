# Importing necessary Flask class and the blueprint
from flask import Flask
from .health import health_blueprint
from .register import register_blueprint
from .login import login_blueprint
# Defining the function register_blueprints
# This function will be responsible for registering all the blueprints of the application
# A blueprint in Flask is a way to organize a group of related views and other code
# It is akin to a mini-application plugged into the main application
def register_blueprints(app: Flask):
    # Registering the health_blueprint with the Flask application instance
    # The blueprint registered here is defined in the 'health' module
    # You can add more blueprints as your application grows
    app.register_blueprint(health_blueprint)
    app.register_blueprint(register_blueprint)
    app.register_blueprint(login_blueprint)
# This file (typically saved as something like routes.py) serves as a central place
# to import and register all your blueprints. This keeps your application's instance creation
# clean and manageable, especially as your application grows and more blueprints are added.
# You just need to import this file and call register_blueprints in your main application file.
