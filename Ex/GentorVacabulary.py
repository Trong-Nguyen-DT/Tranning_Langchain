from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, List
import os
from openai import OpenAI
import re


app = FastAPI()

client = OpenAI(api_key=os.environ['OPEN_AI_KEY'])

class Request(BaseModel):
    word: str

class WordResponse(BaseModel):
    word: str
    meaning: str
    
class Response(BaseModel):
    status: int
    message: str
    data: Any

def process_completion_response(words_with_meaning):
    pairs = words_with_meaning.split("\n")
    results = []
    for pair in pairs:
        if re.match(r'^\d+\. [a-zA-Z-]+: .+$', pair):
            _, word_and_meaning = pair.split(". ")
            word, meaning = word_and_meaning.split(": ")

            word_object = {
                "word": word.strip(),
                "meaning": meaning.strip()
            }
            results.append(word_object)
    return results


def get_similar_words(request):
    word = request.word
    prompt = f"Instructions: You are a student studying English and you want to expand your vocabulary. You decide to use an online tool to generate three English words with similar letters to the given word so you can choose 1 of 4 answers. Make sure the words are created according to the context.\n\nContext: You are studying the word 'personality' in an English textbook. You want to create an exercise that you can do and you need 3 words that are similar to 'personality' to interfere with the answer you choose.\n\nDesired results:\n1. Personnel : Nhân viên\n2. Personal: Riêng tư\n3. Personify : Nhân cách hóa\n\nPlease provide 3 words with similar letters to '{word}':"
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100,
    )
    words = process_completion_response(response.choices[0].text)
    return words

@app.post("/similar-words", response_model=Response)
def get_similar_words_api(request: Request):
    words = get_similar_words(request)

    return Response(status=200, message="Success", data=words)
