from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API token from the environment variable
# The key in getenv must exactly match the name in your .env file
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Check if the token was loaded successfully
if HUGGINGFACEHUB_API_TOKEN is None:
    print("Error: Hugging Face API token not found. Please set HUGGINGFACEHUB_API_TOKEN in your .env file.")
    exit() # Exit if token is not found

# Define the LLM
llm = HuggingFaceEndpoint(
    repo_id="gpt2", # Or the specific model you want to use, e.g., "mistralai/Mistral-Nemo-Instruct-2407"
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
)

# Define prompt templates
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5-line summary on the following text:\n{text}',
    input_variables=['text']
)

# Generate detailed report
prompt1 = template1.format(topic="black hole")
result1 = llm.invoke(prompt1)

# Generate summary
prompt2 = template2.format(text=result1)
result2 = llm.invoke(prompt2)

# Print final result
print("📝 Detailed Report:\n", result1)
print("\n📌 5-Line Summary:\n", result2)