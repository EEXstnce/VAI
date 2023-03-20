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
    "marketing_campaign": PromptTemplate(
        input_variables=["slogan", "company_name"],
        template="What is a good fear-based marketing campaign for {company_name} with the slogan '{slogan}'?",
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
    "goal_benefits": PromptTemplate(
        input_variables=["goal"],
        template="What is the biggest benefit of {goal}?",
    ),
    "goal_outcomes": PromptTemplate(
        input_variables=["goal_benefits"],
        template="What are ways to measure achievement of {goal_benefits}?",
    ),
    "author_book": PromptTemplate(
        input_variables=["author"],
        template="What is the most famous book by {author}?",
    ),
    "book_quote": PromptTemplate(
        input_variables=["author_book"],
        template="The most famous quote from {author_book} is...",
    ),
    "quote_usage": PromptTemplate(
        input_variables=["author_book", "book_quote"],
        template="What are the most famous uses of {book_quote} from people other than {author_book}?",
    ),
}

# Define the dependencies between templates
dependencies = {
    "company_name": [],
    "slogan": ["company_name"],
    "marketing_campaign": ["slogan", "company_name"],
    "expert_name": [],
    "influential_idea": ["expert_name"],
    "idea_quote": ["expert_name", "influential_idea"],
    "goal_benefits": [],
    "goal_outcomes":["goal_benefits"],
    "author_book": [],
    "book_quote":["author_book"],
    "quote_usage":["author_book", "book_quote"]
}
