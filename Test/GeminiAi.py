
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate




GOOGLE_AI_KEY = ""
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_AI_KEY)
prompt = "You are an artificial intelligence. Your task is answer the following question: {input}"

chain = prompt | llm
response = chain.invoke({"input": "Bạn tên là gì?"})

print(response)




