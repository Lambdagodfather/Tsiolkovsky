#Câu 1: Tính thể tích hình cầu bán kính 5
bankinh = 5;
thetich = 4/3 * 3.14 * (bankinh ** 3 )
print("Thể tích hình cầu:", thetich)
#Câu 2: Tính tổng chi phí bán sỉ 60 cuốn sách
def tinh_chi_phi(gia_bia, giam_gia, so_luong):
    gia_sau_giam = gia_bia * (1 - giam_gia)
    tien_sach = gia_sau_giam * so_luong
    tien_ship = 3 + (so_luong - 1) * 0.75
    return tien_sach + tien_ship
print(tinh_chi_phi(24.95, 0.4, 60))