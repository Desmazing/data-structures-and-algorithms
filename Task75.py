# comparison between a shallow copy and deepcopy in lists

import copy

color_list = []

for i in range(5):
	color_list.append(input("Enter colors: "))

print(color_list)

new_list = copy.copy(color_list)

print('Original list', color_list)
print('Copied list', new_list)

# assignment
# get numbers from user, store in list, find products and sum, add both and display to user

num_list = []
for i in range(5):
	num_list.append(int(input("Enter number: ")))

sum = 0
product = 1

for j in num_list:
	sum += j
	product *= j

print('Sum is', sum)
print('Product is', product)