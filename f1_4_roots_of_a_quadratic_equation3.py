import random
from math import sqrt

def get_a():
    return float(input("Enter a: "))
def get_b():
    return float(input("Enter b: "))
def get_c():
    return float(input("Enter c: "))


def find_roots(a, b, c):
    discriminant = b**2 - 4 * a * c
    type(discriminant)

    if discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        return (-b + sqrt(discriminant)) / (2 * a)
    else:
        return

roots = find_roots(get_a(),get_b(),get_c())

if type(roots)==tuple:
    x1 = roots[0]
    x2 = roots[1]
    print("x1 = ", type(x1), "\nx2 = ", type(x2))
elif type(roots)==float:
    print("x = ", type(roots))
else:
    print("No Solution -->", roots)
