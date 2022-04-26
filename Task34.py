# get user input
# add inputs to list
# remove first element... not pop
# display list
# difference between del,pop and remove in lists
# del and pop use index arguments, remove uses value


color_list = []

for i in range(5):
	color_list.append(input('Enter color name: '))

print(color_list)
color_list.pop(0)
# print(color_list.pop(0)) # removes first element
# color_list.pop() # without argument pop removes last element
print(color_list)
