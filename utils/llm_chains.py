from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
from langchain.llms.loading import load_llm
from langchain.llms import OpenAI
from pydantic import BaseModel
from typing import Dict, List
from utils.template_manager import prompt_templates, dependencies
import json
import utils.config as config

# Load the LLM configuration from the JSON file
with open("utils/llm_config.json", "r") as f:
    llm_config = json.load(f)

# Create an instance of the OpenAI class with the loaded LLM configuration
llm = OpenAI(**llm_config)

# Create LLM chains for each prompt template
llm_chains = {key: LLMChain(llm=llm, prompt=prompt_templates[key]) for key in prompt_templates}

def create_llm_chains() -> Dict[str, LLMChain]:
    return {key: LLMChain(llm=llm, prompt=prompt_templates[key]) for key in prompt_templates}

def process_single_chain(chain_key: str, inputs: Dict[str, str], visited: set, results: Dict[str, str], chains: Dict[str, LLMChain]) -> None:
    if chain_key not in visited:
        visited.add(chain_key)
        for dependency in dependencies[chain_key]:
            process_single_chain(dependency, inputs, visited, results, chains)
        required_inputs = {k: inputs[k] for k in chains[chain_key].prompt.input_variables if k in inputs}
        output = chains[chain_key].run(required_inputs)
        results[chain_key] = output
        inputs[chain_key] = output

class CustomSequentialChain(BaseModel):
    llm_chains: Dict[str, LLMChain]
    flow: List[str]

    @property
    def input_keys(self) -> List[str]:
        for key in self.flow:
            if not dependencies[key]:
                return prompt_templates[key].input_variables
        return ['product']

    @property
    def output_keys(self) -> List[str]:
        return self.flow

    def run_chain(self, inputs: Dict[str, str]) -> Dict[str, str]:
        results = {}
        visited = set()

        for key in self.flow:
            process_single_chain(key, inputs, visited, results, self.llm_chains)

        return results
