from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# load the API key
load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

# Invoke the model
result = model.invoke('What is the capital of India')

# Print the result
print(result.content)