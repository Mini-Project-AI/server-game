""" routes/health.py

Function Description:
This function handles health check requests by returning a successful response indicating that the server is connected.

Dependencies:
- Flask: Micro web framework for Python.
- Blueprint: Part of Flask for defining a collection of routes.
- util.generate_response: Module for generating standardized response messages.

Usage:
1. Use this function as a route handler for the '/health-care' endpoint in the Flask application.

"""
from flask import Blueprint
from util.generate_response import response_bad_request, response_ok

health_blueprint = Blueprint('health', __name__)

@health_blueprint.route("/health-care")
def health_care():
    return response_ok("success connect to the server")
