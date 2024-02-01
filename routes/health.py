from flask import Blueprint
from util.generate_response import response_bad_request, response_ok

health_blueprint = Blueprint('health', __name__)

@health_blueprint.route("/health-care")
def health_care():
    return response_ok("success connect to the server")
