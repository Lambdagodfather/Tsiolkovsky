import math

# ================== LỚP POINT ==================
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # Getter
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    # Setter
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    # Tính khoảng cách
    def distance(self, other):
        return math.sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2)


# ================== LỚP LINE SEGMENT ==================
class LineSegment:
    # Constructor (deep copy)
    def __init__(self, p1=None, p2=None):
        if p1 is None:
            self.__d1 = Point()
        else:
            self.__d1 = Point(p1.get_x(), p1.get_y())  # deep copy

        if p2 is None:
            self.__d2 = Point()
        else:
            self.__d2 = Point(p2.get_x(), p2.get_y())  # deep copy

    # Getter
    def get_d1(self):
        return self.__d1

    def get_d2(self):
        return self.__d2

    # Setter
    def set_d1(self, p):
        self.__d1 = Point(p.get_x(), p.get_y())  # deep copy

    def set_d2(self, p):
        self.__d2 = Point(p.get_x(), p.get_y())  # deep copy

    # Độ dài đoạn thẳng
    def length(self):
        return self.__d1.distance(self.__d2)

    # In thông tin
    def inTTin(self):
        print("D1:", self.__d1.get_x(), self.__d1.get_y())
        print("D2:", self.__d2.get_x(), self.__d2.get_y())
        print("Độ dài:", self.length())


# ================== PHẦN CHẠY CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    print("=== TEST LineSegment ===")

    # Tạo điểm
    p1 = Point(1, 2)
    p2 = Point(4, 6)

    # Tạo đoạn thẳng
    line = LineSegment(p1, p2)

    print("\nThông tin đoạn thẳng:")
    line.inTTin()

    # Test deep copy
    print("\nSau khi thay đổi p1:")
    p1.set_x(100)
    p1.set_y(200)

    # Nếu deep copy đúng → line KHÔNG đổi
    line.inTTin()