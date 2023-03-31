from utils.llm_chains import CustomSequentialChain, llm_chains
from utils.template_manager import dependencies
from utils.chat_utils import get_all_steps_in_flow, get_user_input, history, print_output
from utils.result_saving import save_result_to_py, save_result_to_json, save_history_to_json
from typing import Dict, List

from langchain.memory import ChatMessageHistory
from langchain.schema import messages_from_dict, messages_to_dict

# Moved get_all_steps_in_flow to chat_utils
# Moved get_user_input to chat_utils
# Moved print_output to chat_utils
# Moved save_result_to_py to result_saving
# Moved save_result_to_json to result_saving

previous_results = {}

while True:
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

    # Get the initial input(s) from the user or use the previous run results
    inputs = get_user_input(overall_chain.input_keys, previous_results)

    # Run the chains
    result = overall_chain.run_chain(inputs)

    # Print the output
    print_output(overall_chain.output_keys, result)

    dicts = messages_to_dict(history.messages)
    new_messages = messages_from_dict(dicts)

    print(new_messages)

    # Ask the user if they want to save the result to a Python file
    save_to_py = input("Do you want to save the result to a Python file? (y/n) ")
    if save_to_py.lower() == "y":
        save_result_to_py(all_steps, result)
        print("Result saved to a Python file.")
    else:
        print("Result not saved.")

    save_result_to_json(all_steps, result)  # Pass both chain and result to the function

    # Save the result for the next run
    previous_results = result.copy()

    # Ask the user if they want to run the app again
    run_again = input("Do you want to run the app again? (y/n) ")
    if run_again.lower() != "y":
        # Save new_messages to history.json
        save_history_to_json(new_messages)
        break


