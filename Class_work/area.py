import math
radius: float = float(input("Enter the radius of a circle: "))
area = math.pi * radius ** 2
print ("The area of circle with radius", radius, "is", area, sep=" ### ", end="")
print("Done printing")