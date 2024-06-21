import os
from langchain_openai import OpenAI

llm = OpenAI(api_key=os.environ["OPENAI_API_KEY"], model="gpt-3.5-turbo-instruct", temperature=0, max_tokens=512)

for chunk in llm.stream("Onepiece là gì?"):
    print(chunk, end="", flush=True)
