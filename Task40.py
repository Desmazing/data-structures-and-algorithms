# get username
# ensure alphanumeric
# ensure <= 8

name = input('Enter a name: ')

def check_name(nm):
	if nm.isalnum() and len(nm) > 8:
		print('Name is okay')
	else:
		print('Name not okay')

check_name(name)