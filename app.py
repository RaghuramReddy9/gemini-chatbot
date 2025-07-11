import streamlit as st
from modules.gemini_utils import get_gemini_reply

# Set page layout
st.set_page_config(page_title="Ram Intelligent", page_icon="🧠", layout="centered")

# Header
st.markdown("""
    <h1 style='text-align: center; color: #4ade80;'>Ram Intelligent</h1>
    <p style='text-align: center; font-size: 18px;'>Your Smart Gemini AI Assistant</p>
    <hr>
""", unsafe_allow_html=True)

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text input
user_input = st.text_input("Ask me anything 👇")

# Clear button
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()

# Only run Gemini if user types something
if user_input.strip() != "":
    st.session_state.chat_history.append({"role": "user", "text": user_input})
    with st.spinner("Thinking..."):
        try:
            reply = get_gemini_reply(user_input)

            if not reply or reply.strip() == "":
                reply = "⚠️ Gemini didn’t return any answer. Try rephrasing your question."

        except Exception as e:
            reply = f"❌ Error: Something went wrong.\n\nDetails: {e}"

        st.session_state.chat_history.append({"role": "assistant", "text": reply})

elif user_input != "":
    st.warning("⚠️ Please type a question before pressing Enter.")

# Display chat
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"""
            <div style="background-color:#1f2937;padding:10px;border-radius:10px;margin-bottom:5px;color:white;">
                👤 <strong>You:</strong><br>{msg['text']}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color:#4ade80;padding:10px;border-radius:10px;margin-bottom:5px;color:black;">
                🤖 <strong>Ram:</strong><br>{msg['text']}
            </div>
        """, unsafe_allow_html=True)
