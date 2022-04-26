# find minimum from inputs


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

def min_num(num1, num2):
	if a > b:
		print(f'{b} is the min')
	else:
		print(f'{a} is the min')

min_num(a, b)