import os
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage
from langchain_core.output_parsers import StrOutputParser

# Initialize the Llama model
local_llm = "llama3.1"
llm = ChatOllama(model=local_llm, temperature=0)

# Create a prompt template that will accept the log data as an input variable
prompt_template = """You are an AI assistant. Below is a log file:

{log_data}

Please read through these logs carefully. Provide insights on:
1. Why certain actions/requests were denied (if applicable).
2. Why certain errors occurred (if applicable).
3. Any other relevant observations about failures or anomalies.

Keep your explanation concise but thorough.
"""

prompt = PromptTemplate(
    input_variables=["log_data"],
    template=prompt_template
)

def main():
    # Read the log file
    with open("./audit.log", "r") as f:
        log_content = f.read()
    
    # Format the prompt with the log data
    final_prompt = prompt.format(log_data=log_content)
    
    # Convert the prompt into a list of messages for the ChatOllama model
    messages = [HumanMessage(content=final_prompt)]
    
    # Use .invoke(...) to get a single AIMessage (not a ChatResult)
    response = llm.invoke(messages)
    
    # `response` is an AIMessage; get the text from .content
    analysis = response.content
    
    # Print the output
    print(analysis)

if __name__ == "__main__":
    main()