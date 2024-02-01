"""
config/connect.py

Module Description:
This module provides functionality to initialize a MongoDB client and select a database using environment variables.

Dependencies:
- pymongo: Python driver for MongoDB.
- dotenv: Python-dotenv to load environment variables from a .env file.

Usage:
1. Ensure you have a MongoDB server running and accessible.
2. Create a .env file in the root directory of your project and add the following environment variables:
    - MONGO_URI: The URI to connect to your MongoDB server.
    - DB_NAME: The name of the MongoDB database to use.
3. Use the functions provided in this module to connect to the MongoDB server and select the database.

"""

# Import necessary modules
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize MongoDB client using environment variables
mongo_uri = os.getenv('MONGO_URI')  # MongoDB URI from environment variables
db_name = os.getenv('DB_NAME')  # MongoDB database name from environment variables

# Create MongoDB client
client = MongoClient(mongo_uri)

# Select the specified database
db = client[db_name]

# Print message to indicate successful connection
print("Connected to MongoDB")
