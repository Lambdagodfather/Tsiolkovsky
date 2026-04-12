class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def hien_thi(self):
        print(f"Tên: {self.ten}, Vũ khí: {self.vu_khi}, Màu sắc: {self.mau_sac}")


# Danh sách siêu nhân
ds_sieunhan = []

# Nhập dữ liệu
while True:
    print("\nNhập thông tin siêu nhân:")
    ten = input("Tên: ")
    vu_khi = input("Vũ khí: ")
    mau = input("Màu sắc: ")

    sn = SieuNhan(ten, vu_khi, mau)
    ds_sieunhan.append(sn)

    tiep = input("Nhập tiếp không? (y/n): ")
    if tiep.lower() == 'n':
        break

# Hiển thị danh sách
print("\nDanh sách siêu nhân:")
for sn in ds_sieunhan:
    sn.hien_thi()