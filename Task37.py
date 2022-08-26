# get 6 numbers from user
# find square of the first 3... the cube of last 3 numbers

num_list = []

for i in range(6):
	num_list.append(int(input('Enter a number: ')))

for j in range(3):
	print(f'Square of {num_list[j]} is {num_list[j] * num_list[j]}')

for j in range(3, 6):
	print(f'Cube of {num_list[j]} is {num_list[j] * num_list[j] * num_list[j]}')
