import os
from db.fetch_data import fetch_student_data
from utils.prompt_builder import build_prompt
from utils.summarizer import summarize_conversation

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = "your-openai-api-key"  # Temporary for testing
    student_id = "12345"  # Example student ID
    student_data = fetch_student_data(student_id)

    if student_data:
        prompt = build_prompt(student_data)
        summary = summarize_conversation(prompt)

        if summary:
            print("Generated Summary:")
            print(summary)
        else:
            print("Failed to generate a summary.")
    else:
        print("Failed to fetch student data.")
