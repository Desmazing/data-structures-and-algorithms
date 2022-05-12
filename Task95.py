# get number from user


n = int(input("Enter a number: "))
m = 10

for i in range(10, 0, -1):
	if i % 2 != 0:
		print(f'{n} * {i} = {n * i}')