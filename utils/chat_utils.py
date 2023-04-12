# chat_utils.py

import os
from typing import Dict, List
from langchain.memory import ChatMessageHistory
from utils.template_manager import dependencies

history = ChatMessageHistory()

def file_explorer(root_path='.'):
    current_path = root_path
    root_path = os.path.abspath(root_path)  # Get absolute path of the root directory
    while True:
        print(f"Current directory: {os.path.abspath(current_path)}")
        print("Contents:")
        contents = os.listdir(current_path)
        for i, item in enumerate(contents, 1):
            print(f"  {i}. {item}")
        print(f"  {len(contents) + 1}. [Go to parent directory]")
        print(f"  {len(contents) + 2}. [Quit file explorer]")
        
        user_choice = input("Select an option, enter a file name, or type 'q' to quit: ").strip()
        
        if user_choice.lower() == 'q':
            # Quit the file explorer
            return None
        
        try:
            user_choice = int(user_choice)
            if user_choice == len(contents) + 1:
                # Go to parent directory
                parent_path = os.path.dirname(current_path)
                # Check if the parent_path is empty, and if so, set it to the root_path
                parent_path = parent_path if parent_path else root_path
                # Ensure we don't go above the root directory
                if os.path.abspath(parent_path).startswith(root_path):
                    current_path = parent_path
                else:
                    print("Cannot navigate above the root directory.")
            elif user_choice == len(contents) + 2:
                # Quit the file explorer
                return None
            else:
                selected_item = contents[user_choice - 1]
                selected_path = os.path.join(current_path, selected_item)
                if os.path.isdir(selected_path):
                    current_path = selected_path
                else:
                    return selected_path
        except ValueError:
            # User entered a file name
            file_path = os.path.join(current_path, user_choice)
            if os.path.isfile(file_path):
                return file_path
            else:
                print("The specified file does not exist.")
        except IndexError:
            print("Invalid option. Please try again.")


# Function to get all steps in the flow
def get_all_steps_in_flow(flow: str, deps: Dict[str, List[str]]) -> List[str]:
    steps = []
    to_process = [flow]

    while to_process:
        current = to_process.pop()
        steps.append(current)
        to_process.extend(deps[current])

    return list(reversed(steps))

# Add a new function to load file contents
def load_file_contents(file_path: str) -> str:
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return ""
    
    with open(file_path, "r") as f:
        return f.read()

def get_user_input(input_keys: List[str], all_results: Dict[str, List[str]] = None) -> Dict[str, str]:
    inputs = {}
    for key in input_keys:
        value = None  # Initialize the variable 'value' before the loop
        while True:  # Add a loop to re-prompt the user if necessary
            print(f"Enter input for '{key}':")
            print("Options:")
            print("  1. Manual input")
            print("  2. Use previous result")
            print("  3. Load from file")

            user_choice = input("Select an option (1/2/3): ").strip()

            if user_choice == '1':
                # Manual input
                value = input(f"Enter {key}: ")
                history.add_user_message(value)
                break  # Exit the loop

            elif user_choice == '2':
                # Use previous result
                if all_results:
                    option_count = 1
                    options_map = {}
                    for k, values in all_results.items():
                        print(f"Options for {k}:")
                        for v in values:
                            print(f"  {option_count}. {v}")
                            options_map[option_count] = (k, v)
                            option_count += 1

                    result_number = int(input(f"Enter the number of the result you want to use for {key} (1-{len(options_map)}): "))
                    selected_result_key, value = options_map[result_number]
                    break  # Exit the loop
                else:
                    print("No previous results available.")
                    # Continue the loop to prompt the user again for input

            elif user_choice == '3':
                # Load from file using file explorer
                print("File Explorer: (Select a file for input)")

                # Get the user's home directory
                user_home_dir = os.path.expanduser("~")
                # Build the path to the "va" directory dynamically
                va_directory = os.path.join(user_home_dir, "va")

                # Specify the root directory for the file explorer
                file_path = file_explorer(root_path=va_directory)

                # Check if the user chose to quit the file explorer
                if file_path is None:
                    print("File explorer exited. No file selected.")
                    # Continue the loop to prompt the user again for input
                elif os.path.isfile(file_path):
                    value = load_file_contents(file_path)
                    # print(f"Loaded file content: {value}")  # Print loaded file content for debugging
                    break  # Exit the loop
                else:
                    print("The specified file does not exist.")
                    # Continue the loop to prompt the user again for input

        # Update the 'inputs' dictionary after the loop
        if value is not None:
            inputs[key] = value
    return inputs


# Function to print output
def print_output(output_keys: List[str], result: Dict[str, str]) -> None:
    processed_keys = set()
    for key in output_keys:
        if key in processed_keys:
            continue
        processed_keys.add(key)
        history.add_ai_message(result[key])
        print(f"{key.capitalize()}: {result[key]}")

def display_flows_and_get_selection():
    print("Available flows:")
    for i, key in enumerate(dependencies, 1):
        print(f"{i}. {key}")
    user_input = input("Select a flow by entering its number, or type 'quit' or 'q' to exit: ")
    if user_input.lower() in ('quit', 'q'):
        return user_input.lower()
    flow_number = int(user_input)
    selected_flow = list(dependencies)[flow_number - 1]
    return selected_flow
