from llm_chains import CustomSequentialChain, llm_chains
from prompt_templates import dependencies
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
inputs = {}
for key in overall_chain.input_keys:
    value = input(f"Enter {key}: ")
    inputs[key] = value

# Run the chains
result = overall_chain.run_chain(inputs)

# Print the output
for key in overall_chain.output_keys:
    print(f"{key.capitalize()}: {result[key]}")
