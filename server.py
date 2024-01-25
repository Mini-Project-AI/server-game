# Importing necessary modules from Flask
from flask import Flask
# Importing the register_blueprints function from the routes package
from routes import register_blueprints

# Creating an instance of the Flask class
# This instance will act as our WSGI application
app = Flask(__name__)

# Registering blueprints
# Blueprints are a way to organize your Flask application into distinct components
# Here, we are registering the blueprints defined in the routes package to our app
# This helps in keeping the application modular and scalable
register_blueprints(app)

# The conditional __name__ == '__main__' is used to ensure that this script is executed
# only when it is run as the main program, and not when imported as a module in other scripts
# This is a common practice in Python to provide code that runs when the script is run on its own
if __name__ == '__main__':
    # Running the app
    # The run() method of Flask class runs the application on the local development server
    # By default, it runs on http://127.0.0.1:5000/
    # You can also pass different parameters to run() method to change the host, port, debug options etc.
    app.run()

# Note: While this setup is suitable for development, for production environments
# it's recommended to use a more robust WSGI server such as Gunicorn or uWSGI.
