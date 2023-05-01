import math

pi=math.pi
def get_radius():
    return float(input("New radius value please: "))

def get_height():
    return float(input("New height value please: "))

def area_and_volume(r,h):
    area = pi * (r ** 2)
    volume = pi * (r ** 2) * h
    return area, volume

a, v = area_and_volume(get_radius(), get_height())

print(f"Area: {a}\nVolume: {v}")
