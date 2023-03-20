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
        template="What is a good marketing strategy for {company_name} with the slogan '{slogan}'?",
    ),
    "expert_name": PromptTemplate(
        input_variables=["expertise"],
        template="Who is a renowned expert in the field of {expertise}?",
    ),
    "influential_idea": PromptTemplate(
        input_variables=["expert_name"],
        template="What is {expert_name}'s most influential idea?",
    ),
    "idea_quote": PromptTemplate(
        input_variables=["expert_name", "influential_idea"],
        template="What is a famous quote by {expert_name} about {influential_idea}?",
    ),
}

# Define the dependencies between templates
dependencies = {
    "company_name": [],
    "slogan": ["company_name"],
    "marketing_strategy": ["slogan", "company_name"],
    "expert_name": [],
    "influential_idea": ["expert_name"],
    "idea_quote": ["expert_name", "influential_idea"],
}
