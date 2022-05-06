# get sentence
# display last character
# display all chars one by one

sent1 = input("Type your sentence here: ")

print(sent1[-1])

for char in sent1:
	print(char)

# count specific word in a sentence
# use string.count(word) method

word_count = input("Enter the word to count: ")
print(f"{word_count} appears {sent1.count(word_count)} times")