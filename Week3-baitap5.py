import math

# ===== Lớp Point =====
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# ===== Lớp Rectangle =====
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


# ===== Lớp Circle =====
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


# ===== Hàm kiểm tra điểm trong hình tròn =====
def point_in_circle(circle, point):
    d = math.sqrt((point.x - circle.center.x)**2 + (point.y - circle.center.y)**2)
    return d <= circle.radius


# ===== Hàm kiểm tra hình chữ nhật nằm trong hình tròn =====
def rect_in_circle(circle, rect):
    # 4 góc của hình chữ nhật
    p1 = Point(rect.x, rect.y)
    p2 = Point(rect.x + rect.width, rect.y)
    p3 = Point(rect.x, rect.y + rect.height)
    p4 = Point(rect.x + rect.width, rect.y + rect.height)

    return (point_in_circle(circle, p1) and
            point_in_circle(circle, p2) and
            point_in_circle(circle, p3) and
            point_in_circle(circle, p4))


# ===== Hàm kiểm tra có giao nhau =====
def rect_circle_overlap(circle, rect):
    # Kiểm tra nếu có ít nhất 1 góc nằm trong hình tròn
    p1 = Point(rect.x, rect.y)
    p2 = Point(rect.x + rect.width, rect.y)
    p3 = Point(rect.x, rect.y + rect.height)
    p4 = Point(rect.x + rect.width, rect.y + rect.height)

    return (point_in_circle(circle, p1) or
            point_in_circle(circle, p2) or
            point_in_circle(circle, p3) or
            point_in_circle(circle, p4))


# ===== Test =====
c = Circle(Point(0, 0), 5)
p = Point(3, 4)
r = Rectangle(1, 1, 2, 2)

print(point_in_circle(c, p))       # True
print(rect_in_circle(c, r))        # True
print(rect_circle_overlap(c, r))   # True