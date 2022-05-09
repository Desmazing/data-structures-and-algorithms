# sum of first and last num in list

num_lst = []

for i in range(5):
	num_lst.append(int(input("Enter number here: ")))

print(num_lst)
print(f'sum of 1st and last numbers is {num_lst[0] + num_lst[-1]}')

# task
# sum of 2nd and 2nd last num in list

print(f'sum of 2nd and 2nd last numbers is {num_lst[1] + num_lst[-2]}')
