
def area_pol(lst):
    result = 0
    for i in range(len(lst)):
        point1 = lst[i-1]
        point2 = lst[i]
        x1, y1 = point1
        x2, y2 = point2
        area = (x2-x1)*(y2+y1)/2
        result += area

    return abs(result)


coordinates = [(0,0),(0,1),(1,0)]
print(area_pol(coordinates))