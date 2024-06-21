from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
import os
import json
import requests
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def get_current_weather(location, unit="celsius"):
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

def run_conversation(request):
    
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request.question}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=50
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    
    if tool_calls:
        available_functions = {
            "get_current_weather": get_current_weather,
        } 
        messages.append(response_message)
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
            max_tokens=50
        ) 
        return second_response
    return response

class Response(BaseModel):
    status: int
    message: str
    data: Any

class Request(BaseModel):
    question: str
    
@app.post("/api/chat_completion", response_model=Response)
async def chat_completion(request: Request) -> Response:
    data = run_conversation(request).choices[0].message.content
    return Response(status=200, message="success", data=data)
