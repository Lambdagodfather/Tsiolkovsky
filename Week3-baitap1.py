import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def hien_thi(self):
        print(f"({self.x}, {self.y})")

    def doi_xung_qua_O(self):
        return Point(-self.x, -self.y)

    def khoang_cach(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


# Tạo điểm A(3,4)
A = Point(3, 4)
print("Điểm A:", end=" ")
A.hien_thi()

# Nhập điểm B
x = float(input("Nhập x của B: "))
y = float(input("Nhập y của B: "))
B = Point(x, y)

print("Điểm B:", end=" ")
B.hien_thi()

# Tạo điểm C đối xứng B qua O
C = B.doi_xung_qua_O()
print("Điểm C (đối xứng qua O):", end=" ")
C.hien_thi()

# Tính khoảng cách
O = Point(0, 0)
print("Khoảng cách B → O:", B.khoang_cach(O))
print("Khoảng cách A → B:", A.khoang_cach(B))