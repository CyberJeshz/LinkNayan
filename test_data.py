import json
from pathlib import Path

def test_json(filepath):
    try:
        with open(filepath, "r")as file:
            data = json.load(file)
            print(f"File name: {file.name} is valid")
            return True
    except Exception as e:
        print(f"Error: {file.name} {e}")
        return False
    except FileNotFoundError as e:
        print(f"File {file.name} was not found.")
        return False
    except json.JSONDecodeError as e:
        print(f"{file.name} has error: {e}")
        return False;

data_dir = Path("data")
files = ["resources.json", "professionals.json", "hotlines.json"]

print("Testing if this file works:>")

all_valid = True
for filename in files:
    if not test_json(data_dir/filename):
        all_valid = False

if all_valid:
    print("The shit you created worked! :'>")
else:
    print("You gotta work harder man:<")