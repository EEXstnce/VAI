import os

# Check if running in Replit
if "REPLIT_DB_URL" in os.environ:
  # Use Replit Secrets for API key in Replit environment
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
else:
  # Use dotenv for API key in local or non-Replit environment
  from dotenv import load_dotenv

  # Load environment variables from .env file
  load_dotenv()

  # Get the API key from the environment variables
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set up the OpenAI API key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
