import json
from langchain.prompts import PromptTemplate

# Load prompt templates from JSON file
with open("prompt_templates.json", "r") as f:
    prompt_data = json.load(f)

# Create a dictionary of PromptTemplate objects from the loaded data
prompt_templates = {
    key: PromptTemplate(**{k: v for k, v in value.items() if k != '_description'}) 
    for key, value in prompt_data.items()
}

# Load dependencies from the JSON file
with open("dependencies.json", "r") as f:
    dependencies = json.load(f)

