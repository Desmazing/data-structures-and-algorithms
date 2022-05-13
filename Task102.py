# sort student names in ascending order
# display only names with 5 characters
# Task is to add 'A' at the beginning of every name

lst = ['Faith', 'Abel', 'Cain', 'Karen', 'David']

for name in sorted(lst):
	if len(name) == 5:
		print(name)

lst.sort(reverse=True)
print('\n')

for name in lst:
	print(name + 'A')

