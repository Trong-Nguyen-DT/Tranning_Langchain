import os

from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
# Khởi tạo Memory
memory = ConversationBufferMemory()

# Khởi tạo mô hình ngôn ngữ
model = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

# Hàm để tương tác với người dùng và ghi nhớ thông tin
def chat_with_user(input_text):
    # Lấy thông tin từ bộ nhớ (memory)
    previous_info = memory.load_memory_variables({})
    

    # Kết hợp thông tin từ bộ nhớ với câu hỏi của người dùng
    input_text_with_memory = input_text + " " + str(previous_info)

    # Trả lời người dùng và cập nhật bộ nhớ
    response = model.invoke(input_text_with_memory)
    memory.chat_memory.add_user_message(input_text)
    memory.chat_memory.add_ai_message(response)

    return response

# Ví dụ về tương tác với người dùng
user_input = "Tôi đang cần giúp đỡ về môn Toán."
bot_response = chat_with_user(user_input)
print("========================================================")
print(bot_response)
print("========================================================")

# Tương tác tiếp theo với người dùng
user_input_2 = "Tôi cần tìm hiểu về giải tích đa biến."
bot_response_2 = chat_with_user(user_input_2)
print("========================================================")
print(bot_response_2)
print("========================================================")

print(memory.chat_memory)