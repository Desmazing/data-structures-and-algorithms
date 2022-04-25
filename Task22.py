char = input('Enter char: ')

num_list = ['0','1','2','3','4','5','6','7','8','9']
spec_list = ['`','!','~','#','@','%','^','&','*','(',')','[','_','"',';',':','?','<']

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
	print('Vowel')
elif char in num_list:
	print('Number')
elif char in spec_list:
	print('Special character')
else:
	print('Consonant')