import streamlit as st
import time        # for realistic loading simulation
from src.llm_service import generate_linkedin_post

# Page Configuration:
st.set_page_config(
  page_title="Llama3.2 LinkedIn Post Generator",
  page_icon="🚀",
  layout="centered"
)

# Title and Header:
st.title("🚀 Llama3.2 LinkedIn Post Generator (Groq + LangChain)")
st.caption("⚡️ Powered by Groq's super-fast Llama3.2 inference.")

# Note to remind the user of the persona:
st.info(
  "📝 **Persona Set:** Posts are tailored to an **Experienced Architect pivoting to Data Science/AI**, emphasizing structural logic and meticulous execution in the data domain. This aligns with your portfolio goal!"
)

# User input:
topic_input = st.text_area(
  "What topic do you want the LinkedIn post to be about?",
  placeholder="e.g., I just completed a deep learning project that classifies architectural styles using CNNs.",
  height=150
)

# Button to trigger generation:
if st.button("✨ Generate LinkedIn Post", type="primary"):
  # Validation and Generation:
  if not topic_input:
    st.error("Please provide a topic or idea to generate the post.")
  else:
    # Show a loading spinner while the LLM is working:
    with st.spinner("Generating highly engaging post with Llama3.2..."):
      # Simulate the speed of Groq:
      time.sleep(0.5)

      try:
        # Call the core LLM function from src/llm_service.py:
        post_text = generate_linkedin_post(topic_input)

        # Display Result:
        st.subheader("🎉 Your Custom LinkedIn Post:")

        # Display generated text in a blockquote:
        st.markdown(
          f"**Post Preview:**\n> {post_text}",
          unsafe_allow_html=False
        )

        # Add a copy-to-clipboard button:
        st.code(post_text, language="text")

      except Exception as e:
        st.error(f"An error occured: {e}. Check if your Groq API key is valid.")
        st.error("Traceback details are usually printed in the terminal where Streamlit is running.")