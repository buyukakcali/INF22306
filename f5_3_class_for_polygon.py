

class Polygon:
    points: list

    def __init__(self, points: list):
        # print('Given points: ', points)
        self.points = points
        self.total_circumference = 0
        self.total_area = 0

    @property
    def calculate_circumference(self):
        for i in range(len(self.points)):   # [[0, 0], [3, 0], [0, 4]] imagine this list while checking the code
            self.total_circumference += abs(((self.points[i-1][0] - self.points[i][0]) ** 2) + ((self.points[i-1][1] - self.points[i][1]) ** 2)) ** 0.5
        return self.total_circumference

    def calculate_area(self):
        total_area = 0
        for i in range(len(self.points)):   # [[6, 4], [0, 4], [0, 0], [3, 1]] imagine this list while checking the code
            temp_area = ((self.points[i-1][1] + self.points[i][1]) / 2) * (self.points[i-1][0] - self.points[i][0])
            total_area += temp_area
        self.total_area = abs(total_area)
        return self.total_area


if __name__ == '__main__':
    poly = [[6, 4], [0, 4], [0, 0], [3, 1]]     # IMPORTANT: You have to add the points in the correct order

    poly1 = Polygon(poly)

    print(poly1.calculate_circumference)
    print(poly1.calculate_area())
