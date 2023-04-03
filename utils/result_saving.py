import json
import os
import re

from typing import Dict, List

from langchain.schema import messages_to_dict
from utils.chat_utils import history

# Utility function to read JSON data from a file
def read_json_data(filename: str):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

# Function to save the result to a Python file
def save_result_to_py(chain: List[str], result: Dict[str, str]) -> None:
    dir_path = 'code'
    os.makedirs(dir_path, exist_ok=True)

    for key in chain:
        filename = os.path.join(dir_path, f"{key}.py")
        with open(filename, "w") as f:
            f.write(result[key])

    print("Results saved to Python files.")

# Function to save the result to a JSON file, formatted as specified
def save_result_to_json(chain: List[str], result: Dict[str, str]) -> None:
    filename = 'results.json'

    dicts = messages_to_dict(history.messages)
    
    # Create an entry in the desired format
    entry = {
        "chain": chain,
        "result": result
    }
    
    # Load existing data
    existing_data = read_json_data(filename)
    
    # Append new entry to existing data
    existing_data.append(entry)
    
    # Save the updated data to the JSON file
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4)
    
    print("Results appended to JSON file.")

# Function to convert message objects to dictionaries
def message_to_dict(message):
    return {
        'type': message.__class__.__name__,
        'content': message.content,
        'additional_kwargs': message.additional_kwargs
    }

# Updated function to append new_messages to history.json
def save_history_to_json(new_messages):
    # Convert message objects to dictionaries
    new_messages_dicts = [message_to_dict(message) for message in new_messages]

    history_file = 'history.json'
    history_data = read_json_data(history_file)
    history_data.append(new_messages_dicts)

    with open(history_file, 'w') as json_file:
        json.dump(history_data, json_file)


# Function to save a new prompt template and its dependencies
def save_new_prompt_template(new_template_name, new_template_description,
                             new_template_input_variables, new_template_text,
                             new_dependencies):
    # Load existing prompt templates
    with open("prompt_templates.json", "r") as f:
        prompt_templates = json.load(f)

    # Create a new prompt template
    new_template = {
        "_description": new_template_description,
        "input_variables": new_template_input_variables,
        "template": new_template_text
    }

    # Update the prompt_templates dictionary and save it to the JSON file
    prompt_templates[new_template_name] = new_template
    with open("prompt_templates.json", "w") as f:
        json.dump(prompt_templates, f, indent=4)

    # Load existing dependencies
    with open("dependencies.json", "r") as f:
        dependencies = json.load(f)

    # Update the dependencies dictionary and save it to the JSON file
    dependencies[new_template_name] = new_dependencies
    with open("dependencies.json", "w") as f:
        json.dump(dependencies, f, indent=4)

    print("New prompt template and dependency flow created.")

def handle_new_prompt_templates(result, output_key):
    def generate_template_name(template):
        # Use the first three words of the template, remove punctuation, and convert to lowercase
        name_parts = template.split()[:3]
        template_name = "_".join(name_parts).lower()
        template_name = re.sub(r'[^\w\s]', '', template_name)  # Remove punctuation
        
        # Extract input variables from the template
        input_variables = re.findall(r'{(.*?)}', template)
        if input_variables:
            template_name += "_" + "_".join(input_variables)
        return template_name

    for output_key, output_value in result.items():
        if len(output_value) > 10:
            transferable_ideas = output_value.split("\n\n")
            for idx, idea in enumerate(transferable_ideas):
                if not idea.strip():
                    continue
                input_variables_match = re.search(r'input_variables=\[([^]]*?)\]', idea)
                input_variables = []
                if input_variables_match:
                    input_variables_str = input_variables_match.group(1)
                    input_variables = [var.strip('\"') for var in input_variables_str.split(", ")]
                template_match = re.search(r'template="(.*?)"', idea)
                template = template_match.group(1) if template_match else ""
                template_name = generate_template_name(template)
                new_template_name = f"{template_name}"
                new_template_description = f"Template generated from {output_key}"
                save_new_prompt_template(new_template_name, new_template_description, input_variables, template, new_dependencies=[])

def handle_saving_and_user_prompts(all_steps, result, output_key):
    save_to_py = input("Do you want to save the result to a Python file? (y/n) ")
    if save_to_py.lower() == "y":
        save_result_to_py(all_steps, result)
        print("Result saved to a Python file.")
    elif save_to_py.lower() == "n":
        print("Result not saved.")
    
    save_to_template = input("Do you want to save the result to a new prompt template? (y/n) ")
    if save_to_template.lower() == "y":
        handle_new_prompt_templates(result, output_key)
        print("Result saved to a new prompt template.")
    elif save_to_template.lower() == "n":
        print("Result not saved to template.")
    
    save_result_to_json(all_steps, result)
    run_again = input("Do you want to run the app again? (y/n) ")
    return run_again.lower() == "y"