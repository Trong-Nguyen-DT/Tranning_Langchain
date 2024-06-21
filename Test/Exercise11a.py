import os
import json
import requests

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.tools import tool

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
app = FastAPI()
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

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

def run_conversation(question):
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "Hello, how are you doing?"),
            ("ai", "I'm doing well, thanks!"),
            ("human", question),
        ])
    
    messages = prompt.format_messages(name="Tanh")
    llm_with_tools = llm.bind_tools([get_current_weather])
    response = llm_with_tools.invoke(messages)
    if response.tool_calls:
        for tool_call in response.tool_calls:
            if tool_call['name'] == "get_current_weather":
                available_functions = {
                    "get_current_weather" : get_current_weather
                }
                function_name = tool_call["name"]
                function_tool_call = available_functions[function_name]
                tool_response = function_tool_call.invoke(tool_call["args"])
                messages.append(
                    {
                        "tool_call_id": tool_call["id"],
                        "role": "assistant",
                        "name": function_name,
                        "content": tool_response,
                    }
                    
                )
        response = llm.invoke(messages)
    return response.content

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