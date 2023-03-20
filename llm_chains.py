from langchain.chains import LLMChain
from langchain.llms import OpenAI
from pydantic import BaseModel
from typing import Dict, List
from prompt_templates import prompt_templates, dependencies
import config

# Create an OpenAI instance with a high temperature for more randomness
llm = OpenAI(temperature=0.9)

# Create LLM chains for each prompt template
llm_chains = {key: LLMChain(llm=llm, prompt=prompt_templates[key]) for key in prompt_templates}

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

        def process_chain(key: str):
            if key not in visited:
                visited.add(key)
                for dependency in dependencies[key]:
                    process_chain(dependency)
                required_inputs = {k: inputs[k] for k in self.llm_chains[key].prompt.input_variables if k in inputs}
                output = self.llm_chains[key].run(required_inputs)
                results[key] = output
                inputs[key] = output

        for key in self.flow:
            process_chain(key)

        return results
