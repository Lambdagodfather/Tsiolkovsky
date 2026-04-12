from abc import ABC, abstractmethod


# ================== CUSTOM EXCEPTION ==================
class GiaKhongHopLe(Exception):
    pass


# ================== LỚP CHA ABSTRACT ==================
class HangHoa(ABC):
    def __init__(self, ma, ten, gia):
        self.ma = ma
        self.ten = ten
        self.gia = gia

    # PROPERTY
    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe("Giá phải >= 0")
        self._gia = value

    # ABSTRACT METHOD
    @abstractmethod
    def tinhGia(self):
        pass

    # MAGIC METHOD
    def __str__(self):
        return f"{self.ma} - {self.ten} - {self.tinhGia()}"

    def __eq__(self, other):
        return self.ma == other.ma

    def __lt__(self, other):
        return self.tinhGia() < other.tinhGia()


# ================== HÀNG ĐIỆN MÁY ==================
class HangDienMay(HangHoa):
    def __init__(self, ma, ten, gia, baoHanh):
        super().__init__(ma, ten, gia)
        self.baoHanh = baoHanh

    def tinhGia(self):
        return self.gia * 1.1  # thêm thuế


# ================== HÀNG SÀNH SỨ ==================
class HangSanhSu(HangHoa):
    def __init__(self, ma, ten, gia, chatLieu):
        super().__init__(ma, ten, gia)
        self.chatLieu = chatLieu

    def tinhGia(self):
        return self.gia


# ================== HÀNG THỰC PHẨM ==================
class HangThucPham(HangHoa):
    def __init__(self, ma, ten, gia, ngayHH):
        super().__init__(ma, ten, gia)
        self.ngayHH = ngayHH

    def tinhGia(self):
        return self.gia * 0.9  # giảm giá


# ================== DEMO ==================
if __name__ == "__main__":
    try:
        ds = [
            HangDienMay("DM01", "Tivi", 10000, "24 tháng"),
            HangSanhSu("SS01", "Bát", 2000, "Gốm"),
            HangThucPham("TP01", "Sữa", 5000, "01/06/2026")
        ]

        print("\n--- Danh sách ---")
        for h in ds:
            print(h)  # dùng __str__

        print("\n--- Sắp xếp theo giá ---")
        ds.sort()  # dùng __lt__
        for h in ds:
            print(h)

    except GiaKhongHopLe as e:
        print("Lỗi:", e)