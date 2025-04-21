from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = os.getenv("BASE_URL")
