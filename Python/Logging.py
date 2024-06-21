import logging

# Cấu hình logger
logging.basicConfig(filename='example.log', level=logging.INFO)

# Sử dụng logger để ghi lại thông điệp
logging.info('This is an informational message')
logging.warning('This is a warning message')
