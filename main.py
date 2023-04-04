import json
from utils.llm_chains import create_and_run_chain
from utils.chat_utils import history, display_flows_and_get_selection
from utils.result_saving import save_history_to_json, handle_saving_and_user_prompts
from langchain.schema import messages_from_dict, messages_to_dict

class ChatSession:
    def __init__(self):
        self.previous_results = {}
        self.chat_history = []

    def run_chain(self, selected_flow):
        all_steps, result = create_and_run_chain(selected_flow, self.previous_results)
        output_key = list(result.keys())[0]  # Get the key of the result (assumes single output key)
        continue_chat = handle_saving_and_user_prompts(all_steps, result, output_key)
        self.previous_results = result.copy()
        new_messages = messages_from_dict(messages_to_dict(history.messages))
        self.chat_history.extend(new_messages)
        return continue_chat

    def save_history(self):
        save_history_to_json(self.chat_history)

    def chat(self):
        while True:
            selected_flow = display_flows_and_get_selection()
            continue_chat = self.run_chain(selected_flow)
            if not continue_chat:
                self.save_history()
                break

# Start the chat
if __name__ == '__main__':
    chat_session = ChatSession()
    chat_session.chat()
