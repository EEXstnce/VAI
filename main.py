from llm_chains import CustomSequentialChain, llm_chains

# Create the CustomSequentialChain
overall_chain = CustomSequentialChain(llm_chains=llm_chains)

# Get product input from the user
product = input("Enter a product: ")

# Run the chains
result = overall_chain.run_chain({"product": product})

# Print the output
for key in overall_chain.output_keys:
    print(f"{key.capitalize()}: {result[key]}")
