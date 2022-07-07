# calculate circumference and area of a circle
# program to calculate area and circumference of a circle
# simple task is to add half the area and half the circumference
# display all results to users

import math # math module contains many methods to perform mathematical operations


def circumf_area(radius):
	float(input("Enter the circle radius: "))
	c = 2 * math.pi * radius
	a = math.pi * math.pow(radius, 2)
	print(f'Circumference of circle with radius {radius} is {c}')
	print(f'Area of circle with radius {radius} is {a}')
	half_a = a / 2
	half_c = c / 2
	result = half_a + half_c
	print(f'Sum of halves is {result}')

circumf_area(7)
