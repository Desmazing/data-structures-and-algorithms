# check if 1st and last number of a tuple are similar

num_l = []

for i in range(5):
	num_l.append(int(input("Enter numbers here: ")))

num_t = tuple(num_l)

if num_t[0] == num_t[-1]:
	print('1st and last numbers are similar')
else:
	print('Numbers not similar')

# assignment to check on the char similarity of names

names_list = []

for i in range(5):
	names_list.append(input("Enter student names: "))

# addressing the first char of first and last items in the list

if names_list[0][0] == names_list[-1][0]:
	print(names_list[0][0])
	print("chars are similar")

