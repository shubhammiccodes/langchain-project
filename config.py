from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# get the llm env variables from .env
MODEL = os.getenv('MODEL', 'llama3.2:3b')
MODEL_PROVIDER = os.getenv('MODEL_PROVIDER', 'ollama')