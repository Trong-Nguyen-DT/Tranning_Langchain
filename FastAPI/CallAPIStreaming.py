from datetime import datetime
from sseclient import SSEClient

for chunk in SSEClient("http://localhost:8000"):
    print(datetime.now())
    print(chunk, flush=True)
