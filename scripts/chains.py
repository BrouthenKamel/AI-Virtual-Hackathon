from scripts.prompts import *
from scripts.llms import chatGPT

from langchain import LLMChain

general_clustering_chain = LLMChain(llm=chatGPT, prompt=general_clustering_template)

extract_key_points_chain = LLMChain(llm=chatGPT, prompt=extract_key_points_template)