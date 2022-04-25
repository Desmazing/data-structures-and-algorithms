# Get password
# Check it contains alphabet and number

password = input('Enter your password: ')

print(len(password))

if password.isalnum():
	if (len(password)) < 8:
		print('Password okay')
	else:
		print('Too long')
else:
	print('Password not okay. No special chars')
