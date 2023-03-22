from langchain.prompts import PromptTemplate

# Define a library of prompt templates
prompt_templates = {
    # Company inspiration templates
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
    # Expert idea and quote templates
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
    # Goal and benefits templates
    "goal_benefits": PromptTemplate(
        input_variables=["goal"],
        template="What is the biggest benefit of {goal}?",
    ),
    "goal_outcomes": PromptTemplate(
        input_variables=["goal_benefits"],
        template="What are ways to measure achievement of {goal_benefits}?",
    ),
    # Author books and quotes templates
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
    # PRD-related prompt templates
    "product_domain": PromptTemplate(
        input_variables=["product"],
        template="What is the domain or industry of the {product}?",
    ),
    "target_audience": PromptTemplate(
        input_variables=["product_domain"],
        template="Who is the target audience for a product in the {product_domain} domain?",
    ),
    "user_needs": PromptTemplate(
        input_variables=["target_audience"],
        template="What are the main needs of the {target_audience}?",
    ),
    "solution": PromptTemplate(
        input_variables=["user_needs"],
        template="How can a product solve the needs of users with the following needs: {user_needs}?",
    ),
    "product_features": PromptTemplate(
        input_variables=["solution"],
        template="What are the core features of a product that solves the problem with the following solution: {solution}?",
    ),
    "technical_requirements": PromptTemplate(
        input_variables=["product_features"],
        template="Describe the technical requirements of the following product features: {product_features}",
    ),
    "milestones": PromptTemplate(
        input_variables=["product_features"],
        template="What are the development milestones for implementing the following features: {product_features}?",
    ),
    # Meta Prompt templates
    "prpr_1": PromptTemplate(
        input_variables=["domain"],
        template="Collect your thoughts and assume the role of an expert in {domain}. Use the following structure to return 5 prompt that have transferability to other domains and don't reference the given {domain}: \"transferable_idea\": PromptTemplate(        input_variables=[\"input\"],        template=\"your prompt here can wrap {{thing}} if you want or not *end with one of ,.:;?\",    ),",
    ),
    "prpr_2": PromptTemplate(
        input_variables=["domain"],
        template="Imagine that you are an expert in a {domain}, and you want to explore how the concepts and ideas from that domain can be applied to other areas. Using the following relative structure (take some creative liberty occasionally), provide 5 prompts that illustrate transferable ideas that don't reference the original domain explicitly: \"transferable_idea\": PromptTemplate(        input_variables=[\"MUST_BE_PRESENT_INPUT_VAR\"],        template=\"your ideas about {{MUST_BE_PRESENT_INPUT_VAR}} ending in some open ended way\",),    *ensure formatting, don't mention original domain, and end your prompt with ONE of the following not always a question,.:;?",
    ),
    "pr_X": PromptTemplate(
        input_variables=["input"],
        template="Prompt: {input} Response: EXAMPLE",
    ),
    "pr_A": PromptTemplate(
        input_variables=["input"],
        template="{input}",
    ),
    #Emerge templates
    "E_start": PromptTemplate(
        input_variables=["input"],
        template="You are {input}GPT, and expert on the topic of {input}. What is the most interesting thing you know?",
    ),
    "E_two": PromptTemplate(
        input_variables=["E_start"],
        template="You told me this: {E_start} What are the key elements in the least verbose list possible?",
    ),
}

# Define the dependencies between templates
dependencies = {
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
    # Meta dependencies
    "prpr_1": [],
    "prpr_2": [],
    "pr_X": [],
    "pr_A": [],
    # Emerge dependencies
    "E_start": [],
    "E_two": ["E_start"]
    # Emerge Prompt dependencies
}
