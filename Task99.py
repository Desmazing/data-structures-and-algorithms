# get uppercase words from user
# store in list

lst = []

for i in range(5):
	lst.append(input("Enter words here: "))

print("Uppercase words are: ")
for word in lst:
	if word.isupper():
		print(word, end=' ')

print("\nLowercase words are: ")
for word in lst:
	if word.islower():
		print(word, end=' ')