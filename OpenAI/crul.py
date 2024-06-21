import os
from dotenv import load_dotenv
import subprocess

load_dotenv()
api_key = os.getenv('API_KEY')

# Lệnh cURL
curl_command = """
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer {}" \
-d '{{"model": "text-davinci-002", "prompt": "Once upon a time", "max_tokens": 50}}' \
https://api.openai.com/v1/completions
""".format(api_key)

# Thực thi lệnh cURL
subprocess.run(curl_command, shell=True)
