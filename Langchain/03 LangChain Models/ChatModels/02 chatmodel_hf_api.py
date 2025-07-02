# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# # load the API key
# load_dotenv()

# # Initialize the Hugging Face model with the API key
# llm = HuggingFaceEndpoint(
#     # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
#     # huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
# )

# # Use the model for chat
# model = ChatHuggingFace(llm=llm)

# # Invoke the model
# result = model.invoke("What is the capital of India")

# # Print the result
# print(result.content)


from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Use HuggingFaceEndpoint directly
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
)

# Use .invoke() directly
response = llm.invoke("What is the capital of India?")
print(response)
