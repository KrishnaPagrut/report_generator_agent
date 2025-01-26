import os
import psycopg2

def get_postgres_connection():
    try:
        conn = psycopg2.connect(os.getenv("POSTGRES_URI"))
        print("Connected to PostgreSQL successfully!")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None
