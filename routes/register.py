""" routes/register.py

Function Description:
This function handles user registration requests by validating the provided user data and creating a new user in the database if the data is valid.

Dependencies:
- Flask: Micro web framework for Python.
- Blueprint: Part of Flask for defining a collection of routes.
- request: Part of Flask for accessing request data.
- generate_password_hash: Function from Werkzeug for securely hashing passwords.
- jwt: JSON Web Token library for encoding and decoding JWTs.
- config.connect: Module for connecting to the database.
- util.validation_inputs: Module for validating user input data.
- util.generate_response: Module for generating standardized response messages.
- os: Module for interacting with the operating system.
- dotenv: Module for loading environment variables from a .env file.

Usage:
1. Use this function as a route handler for the '/register' endpoint in the Flask application.

"""

from flask import Blueprint, request
from werkzeug.security import generate_password_hash
import jwt
from config.connect import db
from util.validation_inputs import is_valid_email, is_valid_password, is_valid_name, is_valid_age
import datetime
from util.generate_response import response_bad_request, response_create_request
import os
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET')

register_blueprint = Blueprint('register', __name__)

@register_blueprint.route("/register", methods=["POST"])
def register_user():
    data = request.json

    # Validate email
    if not is_valid_email(data.get("email", "")):
        return response_bad_request("Invalid email format")
    
    # Validate password
    if not is_valid_password(data.get("password", "")):
        return response_bad_request("Password must meet the criteria")

    # Validate first and last name
    if not is_valid_name(data.get("first_name", "")) or not is_valid_name(data.get("last_name", "")):
        return response_bad_request("First and last names must be at least 4 characters long")

    # Validate age
    if not is_valid_age(data.get("age", 0)):
        return response_bad_request("Age must be between 6 and 60")
    
    hashed_password = generate_password_hash(data['password'])

    # Check if user already exists
    existing_user = db.users.find_one({"email": data["email"]})
    print(existing_user)
    if existing_user:
        return response_bad_request("User already exists")

    # Create new user
    new_user = {
        "email": data["email"],
        "password": hashed_password,
        "age": data["age"],
        "first_name": data["first_name"],
        "last_name": data["last_name"]
    }
    insert_result = db.users.insert_one(new_user)
    
    new_user.pop("password")
    new_user["_id"] = str(insert_result.inserted_id)

    # Generate JWT token
    token_data = {
        "email": data["email"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # 24 hour expiration
    }
    token = jwt.encode(token_data, JWT_SECRET, algorithm="HS256")

    return  response_create_request( "user created with success",{"user": new_user, "token": token}) 
