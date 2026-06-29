
import streamlit as st
import requests

st.set_page_config(
    page_title="AI Pharma Assistant",
    layout="wide"
)

# Login system
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("AI Pharma Assistant Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()

        else:
            st.error("Invalid credentials")

    st.stop()

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Main App
st.title("AI Pharma Assistant")

st.markdown("### Categories")
st.write("Fever | Pain | Allergy | Acidity | Antibiotic")

question = st.text_input(
    "Ask medicine-related question",
    placeholder="Example: What is paracetamol used for?"
)

if st.button("Ask"):

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"question": question}
    )

    data = response.json()

    answer = data["response"]

    st.session_state.history.append((question, answer))

# Display chat history
st.markdown("## Chat History")

for q, a in reversed(st.session_state.history):

    st.markdown(f"### Question: {q}")
    st.code(a)
