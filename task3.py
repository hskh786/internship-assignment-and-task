import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * math.pow(radius, 2)
print(f"The area of the circle with radius {radius} is: {area}")
circumference = 2 * math.pi * radius
print(f"The circumference of the circle with radius {radius} is: {circumference}")