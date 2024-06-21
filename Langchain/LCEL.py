import os

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any


from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings


app = FastAPI()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

model = ChatOpenAI(model="gpt-3.5-turbo-0125")

class SimilarWord(BaseModel):
    word: str = Field(description="question to set up a joke")
    meaning: str = Field(description="question to set up a joke")

documents = TextLoader("data.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

db = DocArrayInMemorySearch.from_documents(docs, embeddings)
retriever = db.as_retriever()

template = """

Find 10 words that are most similar in spelling to the following word:
{question}

Provide similar words and their meanings in the following format:
- similarWord: {word}, meaning: {meaning}
"""
prompt = ChatPromptTemplate.from_template(template)
output_parser = JsonOutputParser(pydantic_object=SimilarWord)

setup_and_retrieval = RunnableParallel(
    {"question": RunnablePassthrough()}
)
chain = setup_and_retrieval | prompt | model | output_parser

# response = chain.invoke("Tôi sống và làm việc ơ đâu?")

def run_conversation(question):
    return chain.invoke(question)



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