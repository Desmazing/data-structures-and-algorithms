# finding factorial using a loop

num = int(input("Enter a number: "))
y = num
a = 1
while num > 0:
	a =  a * num
	num -= 1

print(f"Factorial of {y} is {a}")