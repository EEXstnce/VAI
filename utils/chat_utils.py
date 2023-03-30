from typing import Dict, List
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()

# Function to get all steps in the flow
def get_all_steps_in_flow(flow: str, deps: Dict[str, List[str]]) -> List[str]:
    steps = []
    to_process = [flow]

    while to_process:
        current = to_process.pop()
        steps.append(current)
        to_process.extend(deps[current])

    return list(reversed(steps))

# Function to get user input
def get_user_input(input_keys: List[str], previous_results: Dict[str, str] = None) -> Dict[str, str]:
    inputs = {}
    for key in input_keys:
        if previous_results:
            print("Previous results:")
            for i, (k, v) in enumerate(previous_results.items(), 1):
                print(f"{i}. {k}: {v}")

            use_previous = input(f"Do you want to use any previous result for {key}? (y/n) ")
            if use_previous.lower() == "y":
                result_number = int(input("Enter the number of the result you want to use: "))
                selected_result_key = list(previous_results.keys())[result_number - 1]
                value = previous_results[selected_result_key]
            else:
                value = input(f"Enter {key}: ")
        else:
            value = input(f"Enter {key}: ")
        history.add_user_message(value)
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
