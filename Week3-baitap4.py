class ConCho:
    def __init__(self, ten, tuoi, mau_long):
        self.ten = ten
        self.tuoi = tuoi
        self.mau_long = mau_long

    def sua(self):
        print(self.ten, "đang sủa")

    def an(self):
        print(self.ten, "đang ăn")

    def chay(self):
        print(self.ten, "đang chạy")


class OTo:
    def __init__(self, hang, mau, toc_do):
        self.hang = hang
        self.mau = mau
        self.toc_do = toc_do

    def chay(self):
        print(self.hang, "đang chạy")

    def dung(self):
        print(self.hang, "đã dừng")

    def tang_toc(self):
        print(self.hang, "đang tăng tốc")


class TaiKhoan:
    def __init__(self, ten_chu, so_du):
        self.ten_chu = ten_chu
        self.so_du = so_du

    def nap_tien(self, tien):
        self.so_du += tien

    def rut_tien(self, tien):
        if tien <= self.so_du:
            self.so_du -= tien
        else:
            print("Không đủ tiền")

    def xem_so_du(self):
        print("Số dư:", self.so_du)
#chuc  nang
cho = ConCho("Milu", 3, "Vàng")
cho.sua()
cho.an()

xe = OTo("Toyota", "Đen", 60)
xe.chay()
xe.tang_toc()

tk = TaiKhoan("Hoang Hiep", 1000)
tk.nap_tien(500)
tk.rut_tien(300)
tk.xem_so_du()