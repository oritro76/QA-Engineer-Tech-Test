import os

from dotenv import find_dotenv, load_dotenv
from loguru import logger

def load_env_variables():
    file = os.path.abspath(__file__)
    project_root = os.path.dirname(file)
    load_dotenv(os.path.join(project_root, ".env"))

load_env_variables()

DEFAULT_MOCK_SERVER_PORT = "5050"
BASE_URL = "https://jsonplaceholder.typicode.com"

if os.environ.get("MOCK_SERVER") == "1":
    BASE_URL = f"http://localhost:{os.environ.get("MOCK_SERVER_PORT", DEFAULT_MOCK_SERVER_PORT)}"
    print("url", BASE_URL)
