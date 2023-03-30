import json
import os
from typing import Dict, List

from langchain.schema import messages_to_dict

# Function to save the result to a Python file
def save_result_to_py(chain: List[str], result: Dict[str, str]) -> None:
    dir_path = 'code'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    for key in chain:
        filename = os.path.join(dir_path, f"{key}.py")
        with open(filename, "w") as f:
            f.write(f"{key} = {result[key]}\n")

        # Remove "key = " prefix from the file
        with open(filename, "r") as f:
            contents = f.read()
        with open(filename, "w") as f:
            f.write(contents.replace(f"{key} = ", ""))

    print("Results saved to Python files.")

# Function to save the result to a JSON file, formatted as specified
def save_result_to_json(chain: List[str], result: Dict[str, str]) -> None:
    filename = 'results.json'
    
    # Create an entry in the desired format
    entry = {
        "chain": chain,
        "result": result
    }
    
    # Check if the file exists and load existing data
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []
    
    # Append new entry to existing data
    existing_data.append(entry)
    
    # Save the updated data to the JSON file
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4)
    
    print("Results appended to JSON file.")