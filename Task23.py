day_name = (input('Enter day name: ')).lower()

if day_name == 'sunday' or day_name == 'sun' or day_name == 'friday' or day_name == 'fri':
	print('Holiday')
else:
	print('Not holiday')