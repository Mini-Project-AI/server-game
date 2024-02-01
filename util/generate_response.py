from typing import Any, List, Union
from flask import jsonify

def generate_response(message: str, status: bool = True, statusCode: int = 200, data: Union[List[Any], Any] = []) -> tuple:
    """
    Generates a standardized JSON response.

    Args:
        message (str): The message to include in the response.
        status (bool, optional): The status of the response. Defaults to True.
        statusCode (int, optional): The HTTP status code. Defaults to 200.
        data (Union[List[Any], Any], optional): The data to include in the response. Defaults to [].

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    return jsonify({
        "message": message,
        "status": status,
        "statusCode": statusCode,
        "data": data
    }), statusCode

def response_not_found(message: str = "Resource not found") -> tuple:
    """
    Generates a '404 Not Found' response.

    Args:
        message (str, optional): The message to include in the response. Defaults to "Resource not found".

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    return generate_response(message, status=False, statusCode=404)

def response_bad_request(message: str = "Bad request") -> tuple:
    """
    Generates a '400 Bad Request' response.

    Args:
        message (str, optional): The message to include in the response. Defaults to "Bad request".

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    return generate_response(message, status=False, statusCode=400)

def response_server_error(message: str = "Internal server error") -> tuple:
    """
    Generates a '500 Internal Server Error' response.

    Args:
        message (str, optional): The message to include in the response. Defaults to "Internal server error".

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    return generate_response(message, status=False, statusCode=500)

def response_not_authorized(message: str = "Not authorized") -> tuple:
    """
    Generates a '401 Unauthorized' response.

    Args:
        message (str, optional): The message to include in the response. Defaults to "Not authorized".

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    return generate_response(message, status=False, statusCode=401)

def response_create_request(message: str = "Resource created successfully", data: Union[List[Any], Any] = [], status: bool = True, statusCode: int = 201) -> tuple:
    """
    Generates a '201 Created' response.

    Args:
        message (str, optional): The message to include in the response. Defaults to "Resource created successfully".
        data (Union[List[Any], Any], optional): The data to include in the response. Defaults to [].
        status (bool, optional): The status of the response. Defaults to True.
        statusCode (int, optional): The HTTP status code. Defaults to 201.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    return generate_response(message, status, statusCode, data)

def response_ok(message: str = "Success", data: Union[List[Any], Any] = [], status: bool = True, statusCode: int = 200) -> tuple:
    """
    Generates a '200 OK' response.

    Args:
        message (str, optional): The message to include in the response. Defaults to "Success".
        data (Union[List[Any], Any], optional): The data to include in the response. Defaults to [].
        status (bool, optional): The status of the response. Defaults to True.
        statusCode (int, optional): The HTTP status code. Defaults to 200.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    return generate_response(message, status, statusCode, data)
