import json
import os
from pathlib import Path
from config import DATA_DIR



def load_json(filename):
    filepath = DATA_DIR/filename
    try:
        with open(filepath, "r")as file:
         data = json.load(file)
         return data
    
    except FileNotFoundError:
       print(f"The file {filepath} is not found")
       return{}
    
    except json.JSONDecodeError as e:
       print(f"Something went wrong: {e}. Please try again")
       return {}
       
    
def save_json(data, filename):
   filepath = DATA_DIR/filename
   try:
      with open(filepath, "w") as file:
         save = json.dump(data, file, indent=4)
      return(f"File {file.name} saved succesfully!")
      
   except Exception as e:
        print(f"Error: {e}")
        return{}


if __name__ == "__main__":
   data = load_json("hotlines.json")
   print(f"saved: {data}")

   print("\nTesting save_json function")
   new_file = {
      "name": "charlie kirk",
      "status": "ambot",
      "version": "1.0"
   }

   result = save_json(new_file, "test_file.json")
   print(result)



