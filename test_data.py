import json
from pathlib import Path

def testJson(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        print(f"{filepath.name} is valuid.")
        return True
    except json.JSONDecodeError as e:
        print(f"{filepath.name} has error: {e}")
        return False
    except FileNotFoundError as e:
        print(f"{filepath.name} not found.")
        return False
    

data_dir = Path("data")
files = ["hotlines.json", "professionals.json", "resources.json"]

print("Testing data files")
all_valid = True
for filename in files:
    if not testJson(data_dir / filename):
        all_valid = False


if all_valid:
    print("Files are valid")
else:
    print("Files have error.")