import os
import json
import requests

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any


from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools.retriever import create_retriever_tool

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
app = FastAPI()
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

@tool
def get_current_weather(location, unit="celsius"):
    """Get the current weather for a given location."""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = os.environ['WEATHER_KEY']
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        temperature = data['main']['temp']
        temperature_str = str(temperature)
        return json.dumps({"location": location.title(), "temperature": temperature_str, "unit": unit})
    else:
        return json.dumps({"error": "Unable to retrieve weather information for the location."})



loader = TextLoader('data.txt')
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512, chunk_overlap=50
)
documents = text_splitter.split_documents(docs)
db = Chroma.from_documents(documents, OpenAIEmbeddings())
retriever = db.as_retriever()
retriever_tool = create_retriever_tool(
    retriever,
    "my_information_search",
    "Search for information about me. For any questions about me, you must use this tool!",
)

tools = [retriever_tool, get_current_weather]

prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI bot. Your name is DT."),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])
    
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    
def run_conversation(question):
    return agent_executor.invoke({"input" : question})['output']

class Response(BaseModel):
    status: int
    message: str
    data: str

class Request(BaseModel):
    question: str

@app.post("/api/chat_completion", response_model=Response)
async def chat_completion(request: Request) -> Response:
    data = run_conversation(request.question)
    return Response(status=200, message="success", data=data)
