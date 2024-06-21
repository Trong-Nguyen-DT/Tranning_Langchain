import threading
import requests

# Hàm chức năng để tải xuống tệp tin
def download_file(url, file_name):
    try:
        response = requests.get(url)
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    except Exception as e:
        print(f"Failed to download {file_name}: {e}")

# Danh sách các tệp tin cần tải xuống với đường link tương ứng
files_to_download = [
    {"url": "https://genk.mediacdn.vn/DlBlzccccccccccccE5CT3hqq3xN9o/Image/2013/12/ViDung/dp-h2-0f3f7.jpg", "file_name": "file1.jpg"},
    {"url": "https://genk.mediacdn.vn/DlBlzccccccccccccE5CT3hqq3xN9o/Image/2013/12/ViDung/dp-h3-0f3f7.jpg", "file_name": "file2.jpg"},
    {"url": "https://i.pinimg.com/originals/22/f3/bf/22f3bfbbafd950df7204a59a6b85a7f9.jpg", "file_name": "file3.jpg"},
    # Thêm các tệp tin khác nếu cần
]

# Tạo một luồng tải xuống cho mỗi tệp tin
threads = []
for file_info in files_to_download:
    url = file_info["url"]
    file_name = file_info["file_name"]
    thread = threading.Thread(target=download_file, args=(url, file_name))
    threads.append(thread)
    thread.start()

# Chờ tất cả các luồng kết thúc
for thread in threads:
    thread.join()

print("All downloads have been completed")
