# dictionary formatting in Python
user_info =  {'name': '',
		'address': '',
		'contact' : ''}

username = input('Enter name: ')
user_info['name'] = username
useraddress = input('Enter address: ')
user_info['address'] = useraddress
usercontact = input('Enter contact: ')
user_info['contact'] = usercontact

print(user_info)
