from utils.llm_chains import create_and_run_chain
from utils.chat_utils import history, display_flows_and_get_selection
from utils.result_saving import save_history_to_json, handle_saving_and_user_prompts
from langchain.schema import messages_from_dict, messages_to_dict

def chat():
    previous_results = {}
    while True:
        selected_flow = display_flows_and_get_selection()
        all_steps, result = create_and_run_chain(selected_flow, previous_results)
        output_key = list(result.keys())[0]  # Get the key of the result (assumes single output key)
        continue_chat = handle_saving_and_user_prompts(all_steps, result, output_key)
        previous_results = result.copy()
        new_messages = messages_from_dict(messages_to_dict(history.messages))
        if not continue_chat:
            save_history_to_json(new_messages)
            break

# Start the chat
if __name__ == '__main__':
    chat()
