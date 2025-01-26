import os
from pymongo import MongoClient

def get_mongo_client():
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        print("Connected to MongoDB successfully!")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
