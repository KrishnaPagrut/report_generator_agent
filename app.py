import os
from dotenv import load_dotenv
from db.fetch_data import fetch_student_data
from utils.prompt_builder import build_prompt
from utils.summarizer import summarize_conversation

# Load environment variables
load_dotenv()

def main():
    # Retrieve the OpenAI API key from environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("Error: OpenAI API key not found in environment variables.")
        return

    # Example student ID (can be replaced with user input or another source)
    student_id = "12345"

    # Fetch student data from databases
    student_data = fetch_student_data(student_id)

    if student_data:
        # Build the OpenAI prompt
        prompt = build_prompt(student_data)

        # Generate summary using OpenAI API
        summary = summarize_conversation(prompt)

        if summary:
            print("Generated Summary:")
            print(summary)
        else:
            print("Failed to generate a summary.")
    else:
        print("Failed to fetch student data.")

if __name__ == "__main__":
    main()
