import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
def get_mongo_client():
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        print("Connected to MongoDB successfully!")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
