pi=3.14
r=float(input("New radius value please: "))
h=float(input("New height value please: "))

cylinder_area = pi * (r**2)
cylinder_volume = cylinder_area * h

print(f"Area of the cylinder is {cylinder_area} and Volume of the cylinder is {cylinder_volume}")