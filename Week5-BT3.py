# ================== LỚP CHA ==================
class CanBo:
    def __init__(self, maCB, hoTen, namSinh):
        self._maCB = maCB
        self._hoTen = hoTen
        self._namSinh = namSinh

    def inTTin(self):
        print("Mã:", self._maCB)
        print("Họ tên:", self._hoTen)
        print("Năm sinh:", self._namSinh)


# ================== CÔNG NHÂN ==================
class CongNhan(CanBo):
    def __init__(self, maCB, hoTen, namSinh, bac):
        super().__init__(maCB, hoTen, namSinh)
        self.bac = bac

    def inTTin(self):
        super().inTTin()
        print("Bậc:", self.bac)


# ================== KỸ SƯ ==================
class KySu(CanBo):
    def __init__(self, maCB, hoTen, namSinh, nganh):
        super().__init__(maCB, hoTen, namSinh)
        self.nganh = nganh

    def inTTin(self):
        super().inTTin()
        print("Ngành:", self.nganh)


# ================== NHÂN VIÊN ==================
class NhanVien(CanBo):
    def __init__(self, maCB, hoTen, namSinh, congViec):
        super().__init__(maCB, hoTen, namSinh)
        self.congViec = congViec

    def inTTin(self):
        super().inTTin()
        print("Công việc:", self.congViec)


# ================== QUẢN LÝ ==================
class QLCB:
    def __init__(self):
        self.ds = []

    # Thêm mới
    def themMoi(self):
        loai = input("Chọn loại (1: Công nhân, 2: Kỹ sư, 3: Nhân viên): ")

        ma = input("Mã: ")
        ten = input("Họ tên: ")
        ns = input("Năm sinh: ")

        if loai == "1":
            bac = int(input("Bậc (1-10): "))
            cb = CongNhan(ma, ten, ns, bac)

        elif loai == "2":
            nganh = input("Ngành: ")
            cb = KySu(ma, ten, ns, nganh)

        elif loai == "3":
            cv = input("Công việc: ")
            cb = NhanVien(ma, ten, ns, cv)

        else:
            print("Loại không hợp lệ!")
            return

        self.ds.append(cb)
        print("✔ Đã thêm!")

    # Tìm kiếm theo tên
    def timKiem(self):
        ten = input("Nhập tên cần tìm: ")
        found = False

        for cb in self.ds:
            if ten.lower() in cb._hoTen.lower():
                print("\n--- Kết quả ---")
                cb.inTTin()
                found = True

        if not found:
            print("❌ Không tìm thấy!")

    # Hiển thị tất cả
    def hienThi(self):
        if not self.ds:
            print("Danh sách trống!")
            return

        print("\n=== DANH SÁCH CÁN BỘ ===")
        for cb in self.ds:
            print("\n----------------")
            cb.inTTin()

    # Menu
    def menu(self):
        while True:
            print("\n===== MENU =====")
            print("1. Thêm mới")
            print("2. Tìm kiếm")
            print("3. Hiển thị")
            print("0. Thoát")

            chon = input("Chọn: ")

            if chon == "1":
                self.themMoi()
            elif chon == "2":
                self.timKiem()
            elif chon == "3":
                self.hienThi()
            elif chon == "0":
                print("Thoát chương trình.")
                break
            else:
                print("Sai lựa chọn!")


# ================== MAIN ==================
if __name__ == "__main__":
    ql = QLCB()
    ql.menu()