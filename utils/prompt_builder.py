def build_prompt(student_data):
    prompt = f"""
    You are an assistant summarizing conversations between students and an academic advising chatbot.
    Your tasks are to:
    1. Extract the **main topic** of discussion.
    2. Identify **actionable items** suggested by the chatbot.
    3. Summarize **student concerns** in one sentence.
    4. Provide a final **summary** of the conversation.
    5. Highlight additional context, challenges, or follow-up actions if relevant.

    Student Information:
    Name: {student_data['name']}
    ID: {student_data['id']}
    Standing: {student_data['standing']}
    Courses Taken: {', '.join(student_data['courses'])}
    Interested Schedules: {', '.join(student_data['schedules'])}
    Chat History:
    {student_data['chats']}

    Output Format:
    Main Topic: [Main topic of the conversation]
    Student Concerns: [A one-sentence summary of the student's concern]
    Actionable Items: 
    - [List actionable suggestions provided by the chatbot]
    Context/Challenges: [Any additional context, challenges, or relevant details]
    Summary: [Final summary of the conversation in a concise paragraph]
    """
    return prompt
