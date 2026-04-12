from abc import ABC, abstractmethod


# ================== CUSTOM EXCEPTION ==================
class TuoiKhongHopLe(Exception):
    pass


class BacKhongHopLe(Exception):
    pass


# ================== LỚP CHA (ABSTRACT) ==================
class CanBo(ABC):
    def __init__(self, hoTen, tuoi, gioiTinh, diaChi):
        self.hoTen = hoTen
        self.tuoi = tuoi
        self.gioiTinh = gioiTinh
        self.diaChi = diaChi

    # PROPERTY TUỔI
    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if value < 18 or value > 65:
            raise TuoiKhongHopLe("Tuổi phải từ 18 đến 65")
        self._tuoi = value

    # ABSTRACT
    @abstractmethod
    def mo_ta(self):
        pass

    # MAGIC METHODS
    def __str__(self):
        return f"{self.hoTen} - {self.tuoi} - {self.gioiTinh} - {self.diaChi} - {self.mo_ta()}"

    def __repr__(self):
        return f"CanBo({self.hoTen}, {self.tuoi})"

    def __eq__(self, other):
        return self.hoTen == other.hoTen and self.tuoi == other.tuoi

    def __lt__(self, other):
        return self.hoTen < other.hoTen


# ================== CÔNG NHÂN ==================
class CongNhan(CanBo):
    def __init__(self, hoTen, tuoi, gioiTinh, diaChi, bac):
        super().__init__(hoTen, tuoi, gioiTinh, diaChi)
        self.bac = bac

    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, value):
        if value < 1 or value > 10:
            raise BacKhongHopLe("Bậc phải từ 1 đến 10")
        self._bac = value

    def mo_ta(self):
        return f"Công nhân bậc {self.bac}"


# ================== KỸ SƯ ==================
class KySu(CanBo):
    def __init__(self, hoTen, tuoi, gioiTinh, diaChi, nganh):
        super().__init__(hoTen, tuoi, gioiTinh, diaChi)
        self.nganh = nganh

    def mo_ta(self):
        return f"Kỹ sư ngành {self.nganh}"


# ================== NHÂN VIÊN ==================
class NhanVien(CanBo):
    def __init__(self, hoTen, tuoi, gioiTinh, diaChi, congViec):
        super().__init__(hoTen, tuoi, gioiTinh, diaChi)
        self.congViec = congViec

    def mo_ta(self):
        return f"Nhân viên làm {self.congViec}"


# ================== QUẢN LÝ ==================
class QLCB:
    def __init__(self):
        self.ds = []

    def them(self, cb):
        self.ds.append(cb)

    def hienThi(self):
        for cb in self.ds:
            print(cb)  # dùng __str__

    def sapXep(self):
        self.ds.sort()  # dùng __lt__

    # LƯU FILE
    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for cb in self.ds:
                f.write(repr(cb) + "\n")

    # ĐỌC FILE (demo đơn giản)
    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print("Đã đọc:", line.strip())


# ================== MAIN ==================
if __name__ == "__main__":
    try:
        ql = QLCB()

        ql.them(CongNhan("Nguyen A", 30, "Nam", "HN", 5))
        ql.them(KySu("Tran B", 40, "Nam", "HCM", "CNTT"))
        ql.them(NhanVien("Le C", 25, "Nu", "DN", "Kế toán"))

        print("\n--- Danh sách ---")
        ql.hienThi()

        print("\n--- Sắp xếp ---")
        ql.sapXep()
        ql.hienThi()

        print("\n--- Lưu file ---")
        ql.save("canbo.txt")

        print("\n--- Đọc file ---")
        ql.load("canbo.txt")

    except (TuoiKhongHopLe, BacKhongHopLe) as e:
        print("Lỗi:", e)