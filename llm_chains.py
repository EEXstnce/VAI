from langchain.chains import LLMChain
from langchain.llms import OpenAI
from pydantic import BaseModel
from typing import Dict, List
from template_manager import prompt_templates, dependencies
import config

# Create an OpenAI instance with a high temperature for more randomness
llm = OpenAI(temperature=0.7)

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
