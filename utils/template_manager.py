import json
from langchain.prompts import PromptTemplate

# Load prompt templates from JSON file
with open("prompt_templates.json", "r") as f:
    prompt_data = json.load(f)

# Create a dictionary of PromptTemplate objects from the loaded data
prompt_templates = {
    key: PromptTemplate(**value) for key, value in prompt_data.items()
}

# Define the dependencies between templates
dependencies = {
    # Meta dependencies
    "pr_A": [],
    "prpr_1": [],
    "prpr_2": [],
    "pr_X": [],
    # Company inspiration dependencies
    "company_name": [],
    "slogan": ["company_name"],
    "marketing_campaign": ["slogan", "company_name"],
    # Expert idea and quote templates
    "expert_name": [],
    "influential_idea": ["expert_name"],
    "idea_quote": ["expert_name", "influential_idea"],
    # Goal and benefits dependencies
    "goal_benefits": [],
    "goal_outcomes":["goal_benefits"],
    # Author books and quotes dependencies
    "author_book": [],
    "book_quote":["author_book"],
    "quote_usage":["author_book", "book_quote"],
    # PRD-related dependencies
    "product_domain": [],
    "target_audience": ["product_domain"],
    "user_needs": ["target_audience"],
    "solution": ["user_needs"],
    "product_features": ["solution"],
    "technical_requirements": ["product_features"],
    "milestones": ["product_features"],

    # Emerge dependencies
    "E_start": [],
    "E_two": ["E_start"],
    # code
    "test":[],
    "front":["test"],
    "bugs":["test", "front"]
}

