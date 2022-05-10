# get names from a list that start from 'f'

names = []

for i in range(5):
	names.append(input("Enter names: "))

for name in names:
	if name.startswith('f'):
		print(name)
print('\n')

for name in names:
	if name.endswith('d'):
		print(name)