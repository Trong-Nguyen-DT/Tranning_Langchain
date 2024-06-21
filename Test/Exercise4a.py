tuDien = {}

while True:
    print("Vui lòng chọn chức năng (bằng số): ")
    print("""
        1. Thêm một từ vựng mới (kèm nghĩa của từ vựng) vào từ điển.
        2. Tra cứu ý nghĩa của một từ vựng.
        3. Cập nhật ý nghĩa cho một từ vựng.
        4. Xóa đi một từ vựng trong từ điển.
        5. Xóa toàn bộ từ vựng trong từ điển.
        6. Xem toàn bộ từ vựng.
        7. Xem toàn bộ từ vựng theo cấu trúc: "TỪ VỰNG" : "Ý NGHĨA".
        8. Kết thúc chương trình.
    """)

    luachon = int(input("Nhập lựa chọn của bạn: "))

    if luachon == 1:
        tuvung = input("Nhập từ vựng: ")
        yNghia = input("Nhập nghĩa của từ vựng: ")
        tuDien[tuvung] = yNghia
        
    elif luachon == 2:
        tuvung_tra = input("Nhập từ vựng cần tra: ")
        if tuvung_tra in tuDien:
            print("Nghĩa của từ", tuvung_tra, "là:", tuDien[tuvung_tra])
        else:
            print("Từ", tuvung_tra, "không có trong từ điển.")

    elif luachon == 3:
        tuvung_capnhat = input("Nhập từ vựng cần cập nhật: ")
        if tuvung_capnhat in tuDien:
            yNghia_moi = input("Nhập nghĩa mới cho từ vựng: ")
            tuDien[tuvung_capnhat] = yNghia_moi
        else:
            print("Từ", tuvung_capnhat, "không có trong từ điển.")

    elif luachon == 4:
        tuvung_xoa = input("Nhập từ vựng cần xóa: ")
        if tuvung_xoa in tuDien:
            del tuDien[tuvung_xoa]
            print("Đã xóa từ", tuvung_xoa, "khỏi từ điển.")
        else:
            print("Từ", tuvung_xoa, "không có trong từ điển.")

    elif luachon == 5:
        tuDien.clear()
        print("Đã xóa toàn bộ từ vựng trong từ điển.")

    elif luachon == 6:
        if not tuDien:
            print("Từ điển hiện đang trống.")
        else:
            print("Danh sách các từ vựng trong từ điển:")
            for tuvung, yNghia in tuDien.items():
                print(tuvung, ":", yNghia)

    elif luachon == 7:
        if not tuDien:
            print("Từ điển hiện đang trống.")
        else:
            print("Cấu trúc của từ điển:")
            for tuvung, yNghia in tuDien.items():
                print('"{}" : "{}"'.format(tuvung, yNghia))

    elif luachon == 8:
        break

    else:
        print("Lựa chọn không chính xác.")
