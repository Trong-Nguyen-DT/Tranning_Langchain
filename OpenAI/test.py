import os



# Lấy giá trị của biến môi trường
api_key = os.getenv('API_KEY')

# Sử dụng giá trị của biến môi trường
print("API Key:", api_key)