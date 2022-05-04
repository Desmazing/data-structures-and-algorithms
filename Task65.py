# program to find area and perimeter of square usingfunction

import math

side = float(input("Enter dimension of square: "))

def sq_calc(s):
	a = s*s
	p = s * 4
	print(f"Area of the square is {a}")
	print(f"Perimeter of the square is {p}")
	sqrt_a = math.sqrt(a)
	sqrt_p = math.sqrt(p)
	add2 = sqrt_a + sqrt_p
	print(f"Final calc is {add2}")

sq_calc(side)