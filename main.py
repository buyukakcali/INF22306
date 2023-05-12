def line_converter(l):
    elements = l.split()
    x1 = float(elements[1].strip(',')[2:])
    y1 = float(elements[2].strip(',')[2:])
    x2 = float(elements[4].strip(',')[2:])
    y2 = float(elements[5].strip(',')[2:])

    return x1, y1, x2, y2


def double_tuple(file):
    result = []
    with open(file) as f:
        lines = f.readlines()
    for i in lines:
        a, b, c, d = line_converter(i)
        ab = (a, b)
        cd = (c, d)
        result += [(ab, cd)]
    return result


print(double_tuple('file.txt'))
