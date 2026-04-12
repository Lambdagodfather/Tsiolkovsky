class NhanVien:
    LUONG_MAX = 50000000   # lương tối đa

    def __init__(self, ten, luongCoBan, heSoLuong):
        self.__ten = ten
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    # ===== Getter =====
    def get_ten(self):
        return self.__ten

    def get_luongCoBan(self):
        return self.__luongCoBan

    def get_heSoLuong(self):
        return self.__heSoLuong

    # ===== Setter =====
    def set_ten(self, ten):
        self.__ten = ten

    def set_luongCoBan(self, luongCoBan):
        if luongCoBan > 0:
            self.__luongCoBan = luongCoBan

    def set_heSoLuong(self, heSoLuong):
        if heSoLuong > 0:
            self.__heSoLuong = heSoLuong

    # ===== Tính lương =====
    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    # ===== Tăng lương =====
    def tangLuong(self, delta):
        luong_moi = self.tinhLuong() + delta
        if luong_moi <= NhanVien.LUONG_MAX:
            self.__luongCoBan += delta / self.__heSoLuong
        else:
            print("Vượt quá lương tối đa!")

    # ===== In thông tin =====
    def inTTin(self):
        print("Tên:", self.__ten)
        print("Lương cơ bản:", self.__luongCoBan)
        print("Hệ số lương:", self.__heSoLuong)
        print("Lương:", self.tinhLuong())


# ===== Test =====
nv = NhanVien("Hiệp", 5000000, 2.5)

nv.inTTin()
print("------")

nv.tangLuong(2000000)
nv.inTTin()