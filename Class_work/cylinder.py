import math

radius: float = float(input("Enter the radius of a cylinder: "))

height: float = float (input ("Enter Height: "))

Area = math.pi * radius ** 2 *  height

print ("The area of a cylinder with  radius", radius, "and height", height, "is", Area,  sep=" ")