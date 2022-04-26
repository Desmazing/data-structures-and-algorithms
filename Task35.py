# get user names, store in a list, display in descending order


names_list = []


for i in range(10):
	names_list.append(input('Enter the name: '))

for j in names_list:
	print(j)

names_list.reverse() #this reverses the order of the list. list methods
names_list.pop()
names_list.pop(0)

for k in names_list:
	print(k)
 