import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load the GROQ_API_KEY from the .env file:
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq Chat model with Llama3.2 and the API key:
if not GROQ_API_KEY:
  raise ValueError("GROQ_API_KEY not found. Please check your .env file.")

llm = ChatGroq(
  temperature=0.7,
  groq_api_key=GROQ_API_KEY,
  model_name="llama-3.2-8b-instruct-fp8"
)

# Define the Prompt Template:
prompt_template = ChatPromptTemplate.from_messages(
  [
    (
      "system",
      "You are an expert LinkedIn content strategist and copywriter. The author is an **experienced architect pivoting into Data Science and AI**. You must generate a highly engaging, professional and viral-ready LinkedIn post based on the user's content, ensuring the tone emphasizes the unique value of their architectural background (Structural Logic, Meticulous Execution, Translating Abstract Concepts) applied to Data and AI. The post must include clear paragraphs, relevant hashtags related to the topic and the career transition and a strong call to action seeking entry-level DATA/AI opportunities or collaborations. Ensure the tone is professional yet enthusiastic."
      ),
    (
      "human",
      "Generate a LinkedIn post about the following topic: {topic}"
    )
  ]
)

# Create the LangChain Processing Chain:
post_chain = prompt_template | llm | StrOutputParser()

def generate_linkedin_post(topic: str) -> str:
  """
  Generates a LinkedIn post using LangChain, Groq and Llama3.2.

  Args:
    topic: Users' input/topic to base the post on.

  Returns:
    Generated LinkedIn post text.
  """
  # Invoke the chain with the users' input topic:
  response = post_chain.invoke({"topic": topic})
  return response

# Example usage for testing:
if __name__ == "__main__":
  test_topic = "I just finished my end-to-end LLM project using Llama3, LangChain and Streamlit. I'm excited to share my learnings on building a fast and efficient GenAI app!"
  print("--- Generated LinkedIn Post ---")
  post = generate_linkedin_post(test_topic)
  print(post)
  print("-" * 50)