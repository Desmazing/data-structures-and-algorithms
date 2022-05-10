# get name from user
# check if lowercase
# if not, convert to lowercase

name = input("Enter username: ")

if name.islower():
	print("Case is okay")
	print(name)
else:
	print("Case needs modifying.")
	name = name.lower()
	print(name)
