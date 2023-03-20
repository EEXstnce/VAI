from langchain.prompts import PromptTemplate

# Define a library of prompt templates
prompt_templates = {
    "company_name": PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    ),
    "slogan": PromptTemplate(
        input_variables=["company_name"],
        template="What is a good slogan for {company_name}?",
    ),
    "marketing_strategy": PromptTemplate(
        input_variables=["slogan", "company_name"],
        template="Write marketing campaign copy for {company_name} with the slogan '{slogan}'?",
    ),
}

# Define the dependencies between templates
dependencies = {
    "company_name": [],
    "slogan": ["company_name"],
    "marketing_strategy": ["slogan", "company_name"],
}

