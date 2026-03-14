import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT/ "data"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    print ("Error.")
    exit(1)

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

MODEL = "openai/gpt-oss-120b:free"

MAX_TOKENS = 1500
TEMPERATURE =  0.7


if DATA_DIR.exists():
    print(f"congrats it exist!")
else:
    print("This file does not exist. Creating file now.")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
if __name__ == '__main__':
    print(f"API loaded: {OPENROUTER_API_KEY[:13]}...")
    print(f"Model loaded: {MODEL}")
    print(f"Base URL: {OPENROUTER_BASE_URL}")
    print(f"DIR directory: {DATA_DIR}")
