# get user number input
# check divisibility by either 5 or 6, or both

num = int(input('Enter a number: '))

if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
	print(f'{num} is divisible by 5 and 6')
elif num % 2 == 0 and num % 3 == 0 and num % 5 != 0:
	print(f'{num} is divisible by 6 but not 5')
elif num % 6 != 0 and num % 5 == 0:
	print(f'{num} is divisible by 5 but not 6')
elif num % 6 != 0 and num % 5 == 0:
	print(f'{num} is divisible by neither 5 nor 6')
