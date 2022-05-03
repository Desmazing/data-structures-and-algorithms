# count number of characters and words in a bio
# simpler solutions
# for characters use len(bio) string method
# for word count use bio.split() method to put the words in a list then count the words with len(list)
bio = input("Enter your bio here: ")

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

char_count = 0

for char in bio.lower():
	if char in alpha:
		char_count += 1
	else:
		char_count = char_count	
print(f"There are {char_count} letters")

word_count = 0
for char in bio:
	if char == ' ':
		word_count += 1
	else:
		word_count += 0

print(f'There are {word_count + 1} words')

print(f'The characters are {len(bio)} in number')
x = bio.split()
print(f'The words are {len(x)} in number')

y = input('Enter a word you want to count: ')
spec_count = 0

for words in x:
	if words == y:
		spec_count += 1
	else:
		spec_count += 0

print(f"The word '{y}' appears {spec_count} times")