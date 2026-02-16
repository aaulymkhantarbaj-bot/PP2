#1 Write a Python program to convert degree to radian.

import math

degree = float(input("Input degree: "))
radian = math.radians(degree)

print("Output radian:", round(radian, 6))

#2 Write a Python program to calculate the area of a trapezoid.
h = int(input())
b1 = int(input())
b2 = int(input())

print("Height:", h)
print("Base, first value:", b1)
print("Base, second value:", b2)
A = ((b1+b2)/2)*h
print("Expected Output:", A)

#3 Write a Python program to calculate the area of regular polygon.
import math
n = int(input("number of sides:"))
a = int(input("length of a side:"))
area = (n * a * a) / (4 * math.tan(math.pi / n))
print(round(area))

#4 Write a Python program to calculate the area of a parallelogram.
b = int(input())
h = int(input())
A = b * h
print("Length of base:", b)
print("Height of parallelogram:", h)
print("Expected Output:", A)
