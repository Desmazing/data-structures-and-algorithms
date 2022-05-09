# print chars from as string that are present at an odd index

words = input("Enter string here: ")

for index in range(1, len(words)):
	if index % 2 != 0:
		print(words[index], end = ' ')

# print chars at an even index number
print('\n')

for index in range(0, len(words)):
	if index % 2 == 0:
		print(words[index], end = ' ')