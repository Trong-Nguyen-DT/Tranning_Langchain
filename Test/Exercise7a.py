from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def home():
    return "Trang Home"

@app.get("/chat_completion")
async def chat_completion(prompt: str):
    # Thực hiện yêu cầu tới OpenAI API
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/completions",
            json={"model": "text-davinci-002", "prompt": prompt},
            headers={"Authorization": "Bearer YOUR_OPENAI_API_KEY"}
        )
        return response.json()
