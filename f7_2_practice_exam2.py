class Polygon(object):
    def __init__(self):
        self.points = []

    def set_points(self, new_points):
        self.points = new_points[:]

    def get_points(self):
        return self.points

    def add_point(self, point):
        self.points += [point]

    def scale(self, factor):
        for i in range(len(self.points)):
            (x, y) = self.points[i]
            self.points[i] = (factor * x, factor * y)

    def move(self, dx, dy):
        new_points = []
        for a_point in self.points:
            x, y = a_point
            new_points += [(x + dx, y + dy)]
            self.set_points(new_points)


if __name__ == '__main__':
    my_points = [(0, 0), (3, 0), (0, 4)]
    next_point = (3, 4)

    p1 = Polygon()
    p1.set_points(my_points)
    p2 = Polygon()
    p2.set_points(my_points)
    print(p1.get_points(), p2.get_points())

    p1.scale(2)
    print(p1.get_points(), p2.get_points())

    p1.move(2, 2)
    print(p1.get_points(), p2.get_points())

    p2.add_point(next_point)
    print(p1.get_points(), p2.get_points())


# print('# Answer 2a----------------------------------------------------')
#
#
# def low_high(x):
#     lowest = 1
#     highest = 1
#     if x > 1:
#         highest = x
#     elif 0 <= x <= 1:
#         lowest = x
#     else:
#         raise ValueError(f"The number {x} is negative! So, you can't calculate the square root")
#     return lowest, highest
#

# def square_root(number, precision):
#     low, high = low_high(number)
#     mid = (low + high) / 2
#     if mid ** 2 > number:
#         low = mid
#         high = number
#     else:
#         high = mid
#         low = 1

# print('# Answer 4a----------------------------------------------------')
# def line_converter(l):
#     elements = l.split()
#     x1 = float(elements[1].strip(',')[2:])
#     y1 = float(elements[2].strip(',')[2:])
#     x2 = float(elements[4].strip(',')[2:])
#     y2 = float(elements[5].strip(',')[2:])
#
#     return x1, y1, x2, y2
#
# print('# Answer 4b----------------------------------------------------')
# def double_tuple(file):
#     result = []
#     with open(file) as f:
#         lines = f.readlines()
#     for i in lines:
#         a, b, c, d = line_converter(i)
#         ab = (a, b)
#         cd = (c, d)
#         result += [(ab, cd)]
#     return result
#
# print(double_tuple('f7_2_practice_exam2_file.txt'))
