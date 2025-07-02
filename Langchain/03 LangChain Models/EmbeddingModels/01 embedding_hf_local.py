# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# # Set your Hugging Face API key
# HUGGINGFACEHUB_API_TOKEN = "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"  # Replace with your actual API key

# # Initialize the Hugging Face model with the API key
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
# )

# # Use the model for chat
# model = ChatHuggingFace(llm=llm)

# # Example Bangladeshi content in English
# bangladesh_content = """
# Bangladesh is a South Asian country with its capital in Dhaka. It is the eighth most populous country in the world.
# The major rivers in Bangladesh are the Padma, Meghna, and Jamuna. The official language is Bengali, and the currency is the Bangladeshi Taka (BDT).
# The country has a rich cultural heritage, with historical landmarks like the Sundarbans, Cox's Bazar, and the Shaheed Minar.
# """

# # Invoke the model with Bangladeshi content
# result = model.invoke(f"Analyze this information: {bangladesh_content}")

# # Print the result
# print(result.content)




from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

# Load your .env
load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize HuggingFace endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
)

# Example content
bangladesh_content = """
Bangladesh is a South Asian country with its capital in Dhaka. It is the eighth most populous country in the world.
The major rivers in Bangladesh are the Padma, Meghna, and Jamuna. The official language is Bengali, and the currency is the Bangladeshi Taka (BDT).
The country has a rich cultural heritage, with historical landmarks like the Sundarbans, Cox's Bazar, and the Shaheed Minar.
"""

# Generate response
response = llm.invoke(f"Analyze this information: {bangladesh_content}")
print(response)
