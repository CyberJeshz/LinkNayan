import json
from pathlib import Path

def test_json(filepath):
    try:
        with open(filepath, "r")as file:
            data = json.load(file)
            print(f"File name: {file.name} is valid")
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False