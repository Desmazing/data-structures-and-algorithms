for i in range(1,6):
	print('* ' * i)

a = 5
b = 1	

while a >= 1:
	while b <= 5:
		print(('  ' * a) + '* ' * b)
		a -= 1
		b += 1

