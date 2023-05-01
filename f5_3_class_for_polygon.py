

class Polygon:
    """Shape of a Triangle with 3 points, point A at the origin"""

    def constructor(self):   # constructor returns tuples
        points = []
        points += [(0, 0)]
        for i in range(self - 1):
            points[i+1]= tuple(input('Enter new point, use comma between two values'))
        return points

    def __init__(self, points:tuple):
        self.points = self.constructor(points)


poly1 = Polygon
poly1.constructor(3)