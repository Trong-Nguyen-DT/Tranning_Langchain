import random

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

def random_number():
    return random.randint(1, 100)

prompt = [SystemMessage(content="Bạn là một trợ lý ảo?"), HumanMessage(content="Hãy cho tôi 1 con số ngẫu nhiên.")]

tools = [{"function": random_number, "description": "Generate a random number"}]

llm = ChatOpenAI(model="gpt-3.5-turbo-1106")
agent = create_openai_functions_agent(llm, tools, prompt) 

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
response = agent_executor.invoke({"input": "Hãy cho tôi 1 con số ngẫu nhiên."})

print(response)
