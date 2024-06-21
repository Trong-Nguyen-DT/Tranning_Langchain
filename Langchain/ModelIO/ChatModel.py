import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

messages = """PS D:\Spring_Boot\RecruitmentSystem> npm start 

phoneshop@0.1.0 start
react-scripts start


Invalid options object. Dev Server has been initialized using an options object that does not match the API schema.        
 - options.allowedHosts[0] should be a non-empty string.
 Lỗi gì đây"""

chat = ChatOpenAI(model="gpt-4-turbo", api_key=os.environ["OPENAI_API_KEY"])

response = chat.invoke(messages)

print(response)