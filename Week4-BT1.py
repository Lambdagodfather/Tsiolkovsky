class NhanVien:
    # Constructor
    def __init__(self, maNV, tenNV, luongCoBan, heSoLuong):
        self.__maNV = maNV
        self.__tenNV = tenNV
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    # Getter
    def get_maNV(self):
        return self.__maNV

    def get_tenNV(self):
        return self.__tenNV

    def get_luongCoBan(self):
        return self.__luongCoBan

    def get_heSoLuong(self):
        return self.__heSoLuong

    # Setter
    def set_luongCoBan(self, luong):
        if luong > 0:
            self.__luongCoBan = luong

    def set_heSoLuong(self, heso):
        if heso > 0:
            self.__heSoLuong = heso

    # Tính lương
    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    # Tăng lương
    def tangLuong(self, delta):
        if delta > 0:
            self.__luongCoBan += delta

    # In thông tin
    def inTTin(self):
        print("Mã NV:", self.__maNV)
        print("Tên NV:", self.__tenNV)
        print("Lương:", self.tinhLuong())


# ================== PHẦN CHẠY CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    print("=== TEST NhanVien ===")

    nv1 = NhanVien("NV01", "Nguyen Van A", 5000, 2.5)

    print("\nThông tin ban đầu:")
    nv1.inTTin()

    print("\nSau khi tăng lương:")
    nv1.tangLuong(1000)
    nv1.inTTin()