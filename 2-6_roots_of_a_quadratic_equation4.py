from math import sqrt

def find_roots(str1):
    a, b, c = str1.split(',')
    a = float(a)
    b = float(b)
    c = float(c)

    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
        result = (x1,x2)
    elif discriminant == 0:
        result = (-b + sqrt(discriminant)) / (2 * a)
    else:
        result = None

    return result


if __name__ == '__main__':
    abc_quadratic = input("Enter the a, b and c values for a quadratic equation, comma(,) between them: ")
    roots = find_roots(abc_quadratic)
    print(f'Root/s of equation is/are : {roots}')

