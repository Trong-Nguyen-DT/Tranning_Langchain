from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()


async def fake_video_streamer():
    for i in range(10):
        print(i)
        time.sleep(0.1)
        yield f"data: Hello {i}"


@app.get("/")
async def main():
    return StreamingResponse(fake_video_streamer(), media_type="text/event-stream")
