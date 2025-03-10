import streamlit as st
from openai import OpenAI

def get_ai_response(subject, question):
    client = OpenAI()
    response = client.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are an ASVAB tutor specializing in {subject}."},
            {"role": "user", "content": question}
        ]
    )
    return response["choices"][0]["message"]["content"]

# Streamlit UI
st.title("ASVAB Study and AI Tutoring")
st.sidebar.header("Study Topics")
topics = ["Arithmetic Reasoning", "Word Knowledge", "Mathematics Knowledge", "General Science", "Paragraph Comprehension", "Electronics Information", "Auto and Shop Information", "Mechanical Comprehension"]
subject = st.sidebar.selectbox("Select a Study Topic", topics)

st.write(f"### {subject} Study Session")
st.write("Use this section to review materials, take practice quizzes, and ask an AI tutor any questions.")

# AI Tutor Interaction
st.write("#### Ask the AI Tutor")
question = st.text_area("Enter your question about this topic:")
if st.button("Get Answer"):
    if question.strip():
        answer = get_ai_response(subject, question)
        st.write("**AI Tutor:**", answer)
    else:
        st.warning("Please enter a question.")

st.sidebar.subheader("Motivational Message")
st.sidebar.write("Stay focused, work hard, and achieve your best! Every study session brings you closer to success.")

