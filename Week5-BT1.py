# ================== LỚP CHA ==================
class HangHoa:
    def __init__(self, maHang, tenHang):
        self._maHang = maHang
        self._tenHang = tenHang

    def inTTin(self):
        print("Mã hàng:", self._maHang)
        print("Tên hàng:", self._tenHang)


# ================== HÀNG ĐIỆN MÁY ==================
class HangDienMay(HangHoa):
    def __init__(self, maHang, tenHang, gia, baoHanh, dienAp, congSuat):
        super().__init__(maHang, tenHang)
        self.gia = gia
        self.baoHanh = baoHanh
        self.dienAp = dienAp
        self.congSuat = congSuat

    def inTTin(self):
        super().inTTin()
        print("Giá:", self.gia)
        print("Bảo hành:", self.baoHanh)
        print("Điện áp:", self.dienAp)
        print("Công suất:", self.congSuat)


# ================== HÀNG SÀNH SỨ ==================
class HangSanhSu(HangHoa):
    def __init__(self, maHang, tenHang, gia, chatLieu):
        super().__init__(maHang, tenHang)
        self.gia = gia
        self.chatLieu = chatLieu

    def inTTin(self):
        super().inTTin()
        print("Giá:", self.gia)
        print("Chất liệu:", self.chatLieu)


# ================== HÀNG THỰC PHẨM ==================
class HangThucPham(HangHoa):
    def __init__(self, maHang, tenHang, gia, ngaySX, ngayHH):
        super().__init__(maHang, tenHang)
        self.gia = gia
        self.ngaySX = ngaySX
        self.ngayHH = ngayHH

    def inTTin(self):
        super().inTTin()
        print("Giá:", self.gia)
        print("Ngày SX:", self.ngaySX)
        print("Ngày HH:", self.ngayHH)


# ================== MAIN TEST ==================
if __name__ == "__main__":
    print("=== TEST HỆ THỐNG HÀNG HÓA ===\n")

    h1 = HangDienMay("DM01", "Tivi", 10000000, "24 tháng", "220V", "150W")
    h2 = HangSanhSu("SS01", "Bát", 50000, "Gốm")
    h3 = HangThucPham("TP01", "Sữa", 30000, "01/01/2026", "01/06/2026")

    print("---- Hàng Điện Máy ----")
    h1.inTTin()

    print("\n---- Hàng Sành Sứ ----")
    h2.inTTin()

    print("\n---- Hàng Thực Phẩm ----")
    h3.inTTin()