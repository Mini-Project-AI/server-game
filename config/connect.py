# config/connect.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Loads the environment variables from the .env file

# Initialize MongoDB client using environment variables
mongo_uri = os.getenv('MONGO_URI')
db_name = os.getenv('DB_NAME')
client = MongoClient(mongo_uri)

# Select your database
db = client[db_name]
print("Connected to MongoDB")
