import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set up the OpenAI API key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
