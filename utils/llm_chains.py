import json
from typing import Dict, List

from pydantic import BaseModel

from langchain.agents import load_tools, initialize_agent
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.llms.loading import load_llm

from utils.template_manager import prompt_templates, dependencies
from utils.chat_utils import get_all_steps_in_flow, get_user_input, print_output
import utils.config as config


def load_llm_configuration(config_path: str) -> Dict:
    """Load the LLM configuration from the JSON file."""
    with open(config_path, "r") as f:
        llm_config = json.load(f)
    return llm_config


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


def create_llm_chains(llm_config: Dict) -> Dict[str, LLMChain]:
    """Create LLM chains for each prompt template."""
    llm = OpenAI(**llm_config)
    return {key: LLMChain(llm=llm, prompt=prompt_templates[key]) for key in prompt_templates}


def process_single_chain(chain_key: str, inputs: Dict[str, str], visited: set, results: Dict[str, str], chains: Dict[str, LLMChain]) -> None:
    """Process a single LLM chain."""
    if chain_key not in visited:
        visited.add(chain_key)
        for dependency in dependencies[chain_key]:
            process_single_chain(dependency, inputs, visited, results, chains)
        required_inputs = {k: inputs[k] for k in chains[chain_key].prompt.input_variables if k in inputs}
        output = chains[chain_key].run(required_inputs)
        results[chain_key] = output
        inputs[chain_key] = output


# Load the LLM configuration from the JSON file
llm_config = load_llm_configuration("utils/llm_config.json")

# Create LLM chains for each prompt template
llm_chains = create_llm_chains(llm_config)

def create_and_run_chain(selected_flow, previous_results):
    all_steps = get_all_steps_in_flow(selected_flow, dependencies)
    overall_chain = CustomSequentialChain(llm_chains=llm_chains, flow=all_steps)
    inputs = get_user_input(overall_chain.input_keys, previous_results)
    result = overall_chain.run_chain(inputs)
    print_output(overall_chain.output_keys, result)
    return all_steps, result