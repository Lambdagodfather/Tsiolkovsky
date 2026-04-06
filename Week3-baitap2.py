class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

sn1 = SieuNhan("Gao", "Đỏ","Vũ Khí: Kiếm" )
sn2 = SieuNhan("Cá Mập"," Xanh" ,"Vũ Khí :Súng")
sn3 = SieuNhan("Quạ Đen","Đen","Mắt")
sn4 = SieuNhan ("Cừu","Trắng","Thiết đầu công")

print(sn1.ten, sn1.vu_khi, sn1.mau_sac)
print(sn2.ten, sn2.vu_khi, sn2.mau_sac)
print(sn3.ten, sn3.vu_khi, sn3.mau_sac)
print(sn4.ten, sn4.vu_khi, sn4.mau_sac)