from flask import jsonify

def generate_response(message, status=True, statusCode=200, data=[]):
    return jsonify({
        "message": message,
        "status": status,
        "statusCode": statusCode,
        "data": data
    }), statusCode

def response_not_found(message="Resource not found"):
    return generate_response(message, status=False, statusCode=404)

def response_bad_request(message="Bad request"):
    return generate_response(message, status=False, statusCode=400)

def response_server_error(message="Internal server error"):
    return generate_response(message, status=False, statusCode=500)

def response_not_authorized(message="Not authorized"):
    return generate_response(message, status=False, statusCode=401)

def response_create_request(message="Resource created successfully",data=[], status=True, statusCode=201):
    return generate_response(message, status, statusCode, data)

def response_ok(message="Success", data=[], status=True, statusCode=200):
    return generate_response(message, status, statusCode, data)
