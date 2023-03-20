# Language Chain Generator

This is a Python project that generates text prompts based on user input. The project includes four files:

- config.py: Sets up the OpenAI API key.
- llm_chains.py: Defines a custom Sequential Chain class that generates language chains using the OpenAI API.
- prompt_templates.py: Defines a library of prompt templates and their dependencies.
- main.py: Runs the language chains using the CustomSequentialChain class.

## Dependencies

The following dependencies are required to run this project:

- python-dotenv: Used to load environment variables.
- openai: Used to generate language chains.

## Usage

1. Clone the repository and navigate to its directory.
2. Install the required dependencies using pip install -r requirements.txt.
3. Create a .env file in the project directory and set the OPENAI_API_KEY environment variable to your OpenAI API key.
4. Run python main.py and enter a product when prompted.
5. The program will output generated prompts for the company name, slogan, and marketing strategy based on the product input.

### Note: The program requires an active internet connection to use the OpenAI API.
