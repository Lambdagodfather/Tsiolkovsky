import time

def bai_time():
    # Lấy thời gian hiện tại (tính bằng giây từ epoch)
    now = time.time()

    # Đổi sang giờ:phút:giây
    local_time = time.localtime(now)
    hour = local_time.tm_hour
    minute = local_time.tm_min
    second = local_time.tm_sec

    print(f"Thời gian hiện tại: {hour:02d}:{minute:02d}:{second:02d}")

    # Tính số ngày từ epoch
    days = now / (24 * 60 * 60)
    print(f"Số ngày từ epoch: {int(days)}")

# Gọi hàm
bai_time()