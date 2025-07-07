import streamlit as st
from crew import FraudDetectionBot


st.set_page_config(page_title="Fraud Detection Bot", page_icon="🤖")

st.title("💳 Fraud Detection Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Paste your transaction data as a JSON list...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # Parse user input as JSON
        import json

        data = json.loads(user_input)
       # if not isinstance(data, list):
        #    raise ValueError("Input must be a list of transactions.")

        # Run the crew with user data
        bot = FraudDetectionBot()
        # Only pass the "data" input as expected by the crew
        result = bot.crew().kickoff(inputs={"data": data})

        # Display the result
        with st.chat_message("assistant"):
            st.markdown("**Detection & Review Results:**")
            st.json(result)
        st.session_state.messages.append(
            {"role": "assistant", "content": f"**Detection & Review Results:**\n\n{result}"}
        )

    except Exception as e:
        error_msg = f"❌ Error: {e}"
        with st.chat_message("assistant"):
            st.error(error_msg)
        st.session_state.messages.append({"role": "assistant", "content": error_msg})
