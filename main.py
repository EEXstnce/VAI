

import json
from utils.llm_chains import create_and_run_chain
from utils.chat_utils import history, display_flows_and_get_selection
from utils.result_saving import save_history_to_json, handle_saving_and_user_prompts
from langchain.schema import messages_from_dict, messages_to_dict


class ChatSession:
    def __init__(self):
        """
        Initializes self.previous_results and self.all_results dictionaries 
        Initializes self.chat_history list 
        """
        self.previous_results = {}
        self.all_results = {}  # Dictionary of lists to store all results
        self.chat_history = []

    def run_chain(self, selected_flow):
        """
        Input: selected_flow (string) 
        Output: continue_chat (string) 
        Calls create_and_run_chain() to get all_steps, result, and chain_executed 
        Calls handle_saving_and_user_prompts() if chain_executed is True 
        Updates self.previous_results and self.all_results dictionaries 
        Updates self.chat_history list with new messages 
        Returns continue_chat 
        """
        all_steps, result, chain_executed = create_and_run_chain(selected_flow, self.all_results)
        if chain_executed:
            # Ask about saving only if the chain was executed
            continue_chat = handle_saving_and_user_prompts(all_steps, result)
        else:
            continue_chat = ""  # Skip saving prompts
        self.previous_results = result.copy()
        # Update all_results by appending each result to its corresponding key
        for key, value in result.items():
            self.all_results.setdefault(key, []).append(value)
        new_messages = messages_from_dict(messages_to_dict(history.messages))
        self.chat_history.extend(new_messages)
        return continue_chat

    def save_history(self):
        """
        Calls save_history_to_json() to save self.chat_history 
        """
        save_history_to_json(self.chat_history)

    def chat(self):
        """
        Loops until user types 'quit' or 'q' 
        Calls display_flows_and_get_selection() to get selected_flow 
        Calls self.run_chain() with selected_flow 
        Calls self.save_history() 
        """
        print("Type 'quit' or 'q' to end the chat at any time.")
        while True:
            selected_flow = display_flows_and_get_selection()
            if selected_flow.lower() in ('quit', 'q'):
                self.save_history()
                print("Chat session ended.")
                break
            continue_chat = self.run_chain(selected_flow)
            self.save_history()
            # Remove the condition to exit the loop based on continue_chat

# Start the chat
if __name__ == '__main__':
    chat_session = ChatSession()
    chat_session.chat()