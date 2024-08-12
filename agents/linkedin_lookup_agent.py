import os
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts.prompt import PromptTemplate
# from langchain_openai import ChatOllama
from langchain_ollama import ChatOllama
from langchain_community.chat_models import ChatOllama
from langchain_core.tools import Tool
from tools.tools import get_profile_url_tavily
from dotenv import load_dotenv

load_dotenv()

def lookup(name: str) -> str:
    llm = ChatOllama(model="llama3", temperature=0)  # Use LLaMA 3

    template = """Given the full name {name_of_person}, get a link to their LinkedIn profile page.
                  Your answer should contain only a URL."""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 LinkedIn profile page",
            func=get_profile_url_tavily,
            description="Useful for getting the LinkedIn Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    
    # Debugging output
    print("Agent Execution Result:", result)
    linked_profile_url = result["output"]
    
    return linked_profile_url














# from dotenv import load_dotenv

# load_dotenv()
# from langchain_openai import ChatOpenAI
# from langchain.prompts.prompt import PromptTemplate
# from langchain_core.tools import Tool
# from langchain.agents import (
#     create_react_agent,
#     AgentExecutor,
# )
# from langchain import hub
# from tools.tools import get_profile_url_tavily


# def lookup(name: str) -> str:
#     llm = ChatOpenAI(
#         temperature=0,
#         model_name="gpt-3.5-turbo",
#     )
#     template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
#                               Your answer should contain only a URL"""

#     prompt_template = PromptTemplate(
#         template=template, input_variables=["name_of_person"]
#     )
#     tools_for_agent = [
#         Tool(
#             name="Crawl Google 4 linkedin profile page",
#             func=get_profile_url_tavily,
#             description="useful for when you need get the Linkedin Page URL",
#         )
#     ]

#     react_prompt = hub.pull("hwchase17/react")
#     agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
#     agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

#     result = agent_executor.invoke(
#         input={"input": prompt_template.format_prompt(name_of_person=name)}
#     )

#     linked_profile_url = result["output"]
#     return linked_profile_url


# if __name__ == "__main__":
#     print(lookup(name="Eden Marco Udemy"))