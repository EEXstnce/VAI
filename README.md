# Language Chain Generator

## Prerequisites

Before you start, make sure you have the following installed:

- Python 3.x
- Pip

## Setting up a Virtual Environment (Optional but Recommended)

It's recommended to run this project in a virtual environment to avoid any version conflicts with other packages you might have installed on your machine. Here's how you can set up a virtual environment:

1. Install virtualenv by running pip install virtualenv.
2. Create a new virtual environment by running virtualenv venv.
3. Activate the virtual environment by running `source venv/bin/activate` on Linux/macOS or venv\Scripts\activate on Windows.##

This is a Python project that generates text prompts based on user input. The project includes several files:

- main.py: The main script that runs the language chains using the CustomSequentialChain class.
- utils/config.py: Loads the environment variables that set up the OpenAI API key.
- utils/template_manager.py: Loads the prompt templates from a JSON file and defines the dependencies between templates.
- utils/chat_utils.py: Contains functions to get user input, print output, and track the conversation history.
- utils/llm_chains.py: Defines a custom Sequential Chain class that generates language chains using the OpenAI API.
- utils/llm_config.json: The configuration file for the OpenAI API.
- utils/result_saving.py: Functions to save the results to Python files and a JSON file.

## Dependencies

The following dependencies are required to run this project:

- python-dotenv: Used to load environment variables.
- openai: Used to generate language chains.

## Usage

1. Clone the repository and navigate to its directory.
2. Install the required dependencies using pip install -r requirements.txt
3. Create a .env file in the project directory and set the OPENAI_API_KEY environment variable to your OpenAI API key.
4. Run python main.py and enter a product when prompted.
5. The program will output generated prompts for the company name, slogan, and marketing strategy based on the product input.

### Note: The program requires an active internet connection to use the OpenAI API.
