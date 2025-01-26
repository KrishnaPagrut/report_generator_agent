from db.mongo_connector import get_mongo_client
from db.postgres_connector import get_postgres_connection

def fetch_student_data(student_id):
    mongo_client = get_mongo_client()
    postgres_conn = get_postgres_connection()

    if not mongo_client or not postgres_conn:
        return None

    # Fetch data from MongoDB
    try:
        student_collection = mongo_client["university"]["students"]
        student_data = student_collection.find_one({"id": student_id}) or {}
    except Exception as e:
        print(f"Error fetching from MongoDB: {e}")
        return None

    # Fetch schedules from PostgreSQL
    try:
        cursor = postgres_conn.cursor()
        cursor.execute("SELECT schedule FROM schedules WHERE student_id = %s", (student_id,))
        student_data["schedules"] = [row[0] for row in cursor.fetchall()]
        cursor.close()
    except Exception as e:
        print(f"Error fetching from PostgreSQL: {e}")
        return None
    finally:
        mongo_client.close()
        postgres_conn.close()

    # Add defaults
    student_data.setdefault("courses", [])
    student_data.setdefault("chats", "No chat history available.")
    student_data.setdefault("schedules", [])

    return student_data
