# find minimum number from list using a function

num_list = []

for i in range(5):
	num_list.append(int(input("Enter a number: ")))

print(num_list)

def min_num(l):
	print(min(l))

min_num(num_list)
