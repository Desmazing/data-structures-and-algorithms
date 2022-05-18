# get password from user
# conditions = alphanumeric chars, >8, <20

def pass_check():
	password = input("Enter password here: ")
	if password.isalnum() and not password.isalpha() and not password.isdigit():
		if 8<(len(password))<20 and " " not in password:
			print("Password okay")
		else:
			print("Password must be between 8 and 20 characters")
			pass_check()
	else:
		print("Include alphanumeric in password")
		pass_check()

pass_check()
	