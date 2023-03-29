from langchain.agents import load_tools, initialize_agent
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import AIMessage, SystemMessage

import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize language models and tools
llm = OpenAI(temperature=0.7)
chat = ChatOpenAI(temperature=0.7)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Initialize agent
agent = initialize_agent(tools, chat, agent="chat-zero-shot-react-description", verbose=True)

# Initialize conversation chain with memory
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])
memory = ConversationBufferMemory(memory_key="history", return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=chat)

# Example conversation loop
while True:
    # Get user input
    user_input = input("You: ")

    # Use agent to generate response
    try:
        agent_response = agent.run(user_input)
    except ValueError as e:
        print(f"Error: {e}")
        if hasattr(e, 'output'):
            print(f"Raw output: {e.output}")
        continue

    # Add agent response to conversation history
    conversation_history = [AIMessage(content=agent_response)]

    # Get conversation response and add it to the memory
    memory.load_memory_variables({"history": []})
    llm_input = {"input": conversation_history[-1].content, "history": memory}

    conversation_response = conversation.run(input=conversation_history[-1].content, history=memory)

    memory.memory[memory.memory_key].append(SystemMessage(content=conversation_response))



    # Print conversation response and memory contents
    print("Bot:", conversation_response)
    print("Memory contents:")
    for message in memory.memory:
        print(message.content)
