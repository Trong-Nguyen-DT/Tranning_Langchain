from openai import OpenAI
import os


client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)

# import openai

# # Thay thế 'YOUR_API_KEY' bằng API Key của bạn
# openai.api_key = 'YOUR_API_KEY'

# # Gửi yêu cầu tạo văn bản
# response = openai.Completion.create(
#     engine="text-davinci-002",  # Chọn mô hình bạn muốn sử dụng
#     prompt="Once upon a time",
#     max_tokens=50
# )

# # In kết quả
# print(response.choices[0].text.strip())
