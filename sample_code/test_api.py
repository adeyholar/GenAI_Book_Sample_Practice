from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access API key
api_key = os.getenv("GROQ_API_KEY")
print(f"API Key: {api_key}")