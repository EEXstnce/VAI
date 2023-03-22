import json
import os
from llm_chains import CustomSequentialChain, llm_chains, create_llm_chains
from template_manager import dependencies
from typing import Dict, List

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
def get_user_input(input_keys: List[str]) -> Dict[str, str]:
    inputs = {}
    for key in input_keys:
        value = input(f"Enter {key}: ")
        inputs[key] = value
    return inputs

# Function to print output
def print_output(output_keys: List[str], result: Dict[str, str]) -> None:
    processed_keys = set()
    for key in output_keys:
        if key in processed_keys:
            continue
        processed_keys.add(key)
        print(f"{key.capitalize()}: {result[key]}")

# Function to save the result to a JSON file
def save_result_to_json(chain: List[str], result: Dict[str, str], filename: str = "results.json") -> None:
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []

    result_with_chain = {
        "chain": chain,
        "result": result
    }
    data.append(result_with_chain)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)



# Get the desired flow from the user
print("Available flows:")
for i, key in enumerate(dependencies, 1):
    print(f"{i}. {key}")

flow_number = int(input("Select a flow by entering its number: "))
selected_flow = list(dependencies.keys())[flow_number - 1]

# Get all steps in the selected flow
all_steps = get_all_steps_in_flow(selected_flow, dependencies)

# Create the CustomSequentialChain with the selected flow
overall_chain = CustomSequentialChain(llm_chains=llm_chains, flow=all_steps)

# Get the initial input(s) from the user
inputs = get_user_input(overall_chain.input_keys)

# Run the chains
result = overall_chain.run_chain(inputs)

# Print the output
print_output(overall_chain.output_keys, result)

# Save the result to a JSON file
save_result_to_json(all_steps, result)

