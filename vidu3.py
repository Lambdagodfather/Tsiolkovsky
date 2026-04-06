# ===== Lớp cha =====
class CanBo:
    def __init__(self, hoten, tuoi, gioitinh, diachi):
        self.hoten = hoten
        self.tuoi = tuoi
        self.gioitinh = gioitinh
        self.diachi = diachi

    def hien_thi(self):
        print(f"Họ tên: {self.hoten}, Tuổi: {self.tuoi}, "
              f"Giới tính: {self.gioitinh}, Địa chỉ: {self.diachi}")


# ===== Lớp con =====
class CongNhan(CanBo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, bac):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.bac = bac

    def hien_thi(self):
        super().hien_thi()
        print(f"Bậc: {self.bac}")


class KySu(CanBo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, nganh):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.nganh = nganh

    def hien_thi(self):
        super().hien_thi()
        print(f"Ngành: {self.nganh}")


class NhanVien(CanBo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, congviec):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self.congviec = congviec

    def hien_thi(self):
        super().hien_thi()
        print(f"Công việc: {self.congviec}")


# ===== Quản lý cán bộ =====
class QLCB:
    def __init__(self):
        self.danhsach = []

    def themmoi(self):
        print("Nhập vào 1.Công nhân / 2.Kỹ sư / 3.Nhân viên")
        loai = input("Chọn: ")

        hoten = input("Nhập họ tên: ")
        tuoi = input("Nhập tuổi: ")
        gioitinh = input("Nhập giới tính: ")
        diachi = input("Nhập địa chỉ: ")

        if loai == "1":
            bac = input("Nhập bậc: ")
            cb = CongNhan(hoten, tuoi, gioitinh, diachi, bac)

        elif loai == "2":
            nganh = input("Nhập ngành: ")
            cb = KySu(hoten, tuoi, gioitinh, diachi, nganh)

        elif loai == "3":
            congviec = input("Nhập công việc: ")
            cb = NhanVien(hoten, tuoi, gioitinh, diachi, congviec)

        else:
            print("Lựa chọn không hợp lệ!")
            return

        self.danhsach.append(cb)
        print("✔ Thêm thành công!")

    def timkiem(self):
        ten = input("Nhập tên cần tìm: ")
        for cb in self.danhsach:
            if ten.lower() in cb.hoten.lower():
                cb.hien_thi()

    def hienthi_ds(self):
        print("===== DANH SÁCH CÁN BỘ =====")
        for cb in self.danhsach:
            cb.hien_thi()
            print("------------------")


# ===== MENU =====
ql = QLCB()

while True:
    print("\n===== MENU =====")
    print("1. Thêm cán bộ")
    print("2. Tìm kiếm theo tên")
    print("3. Hiển thị danh sách")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        ql.themmoi()
    elif chon == "2":
        ql.timkiem()
    elif chon == "3":
        ql.hienthi_ds()
    elif chon == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Sai lựa chọn!")