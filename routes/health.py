from flask import Blueprint

health_blueprint = Blueprint('health', __name__)

@health_blueprint.route("/health-care")
def health_care():
    return {
        "message": "success connect to the server",
        "status": True,
        "statusCode": 200
    }
