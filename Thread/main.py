import threading
import time

# Định nghĩa một hàm để in số nguyên từ 1 đến n
def in_so_nguyen(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(1)

# Tạo các luồng
thread1 = threading.Thread(target=in_so_nguyen, args=(5,))
thread2 = threading.Thread(target=in_so_nguyen, args=(5,))

# Khởi động các luồng
thread1.start()
thread2.start()

# Đợi các luồng hoàn thành
thread1.join()
thread2.join()

print("Kết thúc chương trình")
