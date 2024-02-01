""" routes/login.py

Function Description:
This function handles user login by validating the provided email and password,
fetching the user from the database, verifying the password, and generating a JWT token upon successful login.

Dependencies:
- Flask: Micro web framework for Python.
- Blueprint: Part of Flask for defining a collection of routes.
- request: Module for handling HTTP request data.
- check_password_hash: Function for verifying password hashes.
- jwt: JSON Web Token implementation.
- os: Module for interacting with the operating system.
- load_dotenv: Function to load environment variables from a .env file.
- config.connect: Module for connecting to the MongoDB database.
- util.validation_inputs: Module for input validation functions.
- util.generate_response: Module for generating standardized response messages.

Usage:
1. Ensure that the environment variables are set, including the JWT_SECRET key.
2. Use this function as a route handler for the '/login' endpoint in the Flask application.

"""
from flask import Blueprint, request
from werkzeug.security import check_password_hash
import jwt
from config.connect import db
from util.validation_inputs import is_valid_email, is_valid_password
import datetime
from util.generate_response import response_bad_request, response_ok, response_not_found
import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv('JWT_SECRET')

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route("/login", methods=["POST"])
def login_user():

    data = request.json

    # Validate email
    if not is_valid_email(data.get("email", "")):
        return response_bad_request("Invalid email format")
    
    # Validate password
    if not is_valid_password(data.get("password", "")):
        return response_bad_request("Password must meet the criteria")

    # Fetch user from DB
    user = db.users.find_one({"email": data["email"]})
    if not user:
        return response_not_found("User not found")

    # Verify password
    if not check_password_hash(user['password'], data['password']):
        return response_bad_request("Invalid credentials")

    user_data = {
    "user_id": str(user['_id']),  # Convert ObjectId to string
    "email": user['email'],
    "first_name": user['first_name'],
    "last_name": user['last_name'],
    }
    
    # Generate JWT token
    token_data = {
    "email": user["email"],
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    token = jwt.encode(token_data, JWT_SECRET, algorithm="HS256")

    return  response_ok( "user login with success",{"user": user_data, "token": token}) 
