# ================== LỚP CHA ==================
class NhanVien:
    def __init__(self, maNV, tenNV, luongCoBan):
        self._maNV = maNV
        self._tenNV = tenNV
        self._luongCoBan = luongCoBan

    def tinhLuong(self):
        return self._luongCoBan

    def inTTin(self):
        print("Mã NV:", self._maNV)
        print("Tên NV:", self._tenNV)
        print("Lương:", self.tinhLuong())


# ================== CỘNG TÁC VIÊN ==================
class CongTacVien(NhanVien):
    def __init__(self, maNV, tenNV, luongCoBan, thoiHanHD, phuCapLD):
        super().__init__(maNV, tenNV, luongCoBan)
        self.thoiHanHD = thoiHanHD
        self.phuCapLD = phuCapLD

    def tinhLuong(self):
        return self._luongCoBan + self.phuCapLD

    def inTTin(self):
        super().inTTin()
        print("Thời hạn HĐ:", self.thoiHanHD)
        print("Phụ cấp lao động:", self.phuCapLD)


# ================== NHÂN VIÊN CHÍNH THỨC ==================
class NhanVienChinhThuc(NhanVien):
    def __init__(self, maNV, tenNV, luongCoBan, viTri):
        super().__init__(maNV, tenNV, luongCoBan)
        self.viTri = viTri

    def inTTin(self):
        super().inTTin()
        print("Vị trí:", self.viTri)


# ================== TRƯỞNG PHÒNG ==================
class TruongPhong(NhanVien):
    def __init__(self, maNV, tenNV, luongCoBan, ngayQL, phuCapQL):
        super().__init__(maNV, tenNV, luongCoBan)
        self.ngayQL = ngayQL
        self.phuCapQL = phuCapQL

    def tinhLuong(self):
        return self._luongCoBan + self.phuCapQL

    def inTTin(self):
        super().inTTin()
        print("Ngày quản lý:", self.ngayQL)
        print("Phụ cấp quản lý:", self.phuCapQL)


# ================== MAIN TEST ==================
if __name__ == "__main__":
    print("=== TEST NHÂN VIÊN ===\n")

    nv1 = CongTacVien("CTV01", "Nguyen A", 3000, "6 tháng", 500)
    nv2 = NhanVienChinhThuc("NV01", "Tran B", 7000, "Kỹ sư")
    nv3 = TruongPhong("TP01", "Le C", 10000, "01/01/2024", 2000)

    print("---- Cộng tác viên ----")
    nv1.inTTin()

    print("\n---- Nhân viên chính thức ----")
    nv2.inTTin()

    print("\n---- Trưởng phòng ----")
    nv3.inTTin()