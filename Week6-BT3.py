import math

# ================== CUSTOM EXCEPTION ==================
class MauSoBangKhong(Exception):
    pass


# ================== LỚP PHÂN SỐ ==================
class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise MauSoBangKhong("Mẫu số không được bằng 0")
        self.__tu = tu
        self.__mau = mau
        self.toi_gian()

    # ================== GETTER ==================
    @property
    def tu(self):
        return self.__tu

    @property
    def mau(self):
        return self.__mau

    # ================== TỐI GIẢN ==================
    def toi_gian(self):
        gcd = math.gcd(self.__tu, self.__mau)
        self.__tu //= gcd
        self.__mau //= gcd

        if self.__mau < 0:
            self.__tu *= -1
            self.__mau *= -1

    def is_toi_gian(self):
        return math.gcd(self.__tu, self.__mau) == 1

    # ================== TOÁN TỬ ==================
    def __add__(self, other):
        return PhanSo(
            self.__tu * other.__mau + other.__tu * self.__mau,
            self.__mau * other.__mau
        )

    def __sub__(self, other):
        return PhanSo(
            self.__tu * other.__mau - other.__tu * self.__mau,
            self.__mau * other.__mau
        )

    def __mul__(self, other):
        return PhanSo(
            self.__tu * other.__tu,
            self.__mau * other.__mau
        )

    def __truediv__(self, other):
        if other.__tu == 0:
            raise MauSoBangKhong("Không thể chia cho phân số 0")
        return PhanSo(
            self.__tu * other.__mau,
            self.__mau * other.__tu
        )

    # ================== SO SÁNH ==================
    def __eq__(self, other):
        return self.__tu * other.__mau == other.__tu * self.__mau

    def __lt__(self, other):
        return self.__tu * other.__mau < other.__tu * self.__mau

    def __gt__(self, other):
        return self.__tu * other.__mau > other.__tu * self.__mau

    # ================== HIỂN THỊ ==================
    def __str__(self):
        if self.__mau == 1:
            return f"{self.__tu}"
        return f"{self.__tu}/{self.__mau}"


# ================== MAIN ==================
if __name__ == "__main__":
    ds = []

    n = int(input("Nhập số lượng phân số: "))

    for i in range(n):
        print(f"\nPhân số {i+1}:")
        tu = int(input("Tử: "))
        mau = int(input("Mẫu: "))

        try:
            ps = PhanSo(tu, mau)
            ds.append(ps)
        except MauSoBangKhong as e:
            print("Lỗi:", e)

    print("\n--- Dạng tối giản ---")
    for ps in ds:
        print(ps)

    print("\n--- Sắp xếp tăng dần ---")
    ds_sorted = sorted(ds)
    for ps in ds_sorted:
        print(ps)