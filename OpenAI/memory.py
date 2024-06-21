import openai

# Đặt khóa API OpenAI của bạn
openai.api_key = 'YOUR_API_KEY'

# Xác định prompt ban đầu và bộ nhớ
initial_prompt = "Khởi tạo bộ nhớ."
initial_memory = []

# Xác định prompt tiếp theo
subsequent_prompt = "Tiếp tục cuộc trò chuyện."

# Gửi yêu cầu với bộ nhớ
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=subsequent_prompt,
    max_tokens=50,
    temperature=0.7,
    memory={"data": initial_memory},
)

# Cập nhật bộ nhớ với phản hồi
initial_memory = response['choices'][0]['memory']['data']
