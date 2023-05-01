import math

pi=math.pi          # real pi
def get_radius():   # It is function to get the radius easily in everywhere.
                    # Also it can be used for circle, sphere or any other wanted 'radius'
    return float(input("Radius value please: "))

def get_height():   # It is function to get the heihgt easily in everywhere
                    # Also it can be used for cylinder, cube, pyramid or any other wanted 'height'
    return float(input("Height value please: "))


def surface_and_volume(r,h):    # for surface and volume calculation of cylinder
    surface = 2 *pi * (r ** 2) + 2 * pi * r * h
    volume = pi * (r ** 2) * h
    return surface, volume

def trial():        # for testing the code
    while True:
        test_end = input(
            "If you want to quit from test, just press \"q\" or \"Q\", otherwise press any key to continue to test: ")
        if test_end.lower() != "q":
            rad = get_radius()
            hgt = get_height()
            a, v = surface_and_volume(rad,hgt)
            print(f"Surface: {a}\nVolume: {v}")
        else:
            break

if __name__ == '__main__':
    trial()