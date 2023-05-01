pi=3.14
def get_radius():
    return float(input("New radius value please: "))

def get_height():
    return float(input("New height value please: "))


def calc_surface(r):
    return pi * (r ** 2)

def calc_volume(r,h):
    return calc_surface(r) * h

print(f"Area of the cylinder is {calc_surface(get_radius())}")

print(f"Volume of the cylinder is {calc_volume(get_radius(),get_height())}")