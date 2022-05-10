# get sentence from user
# system should display only ten chars max
# could use string slicing

sentence = input("Enter sentence here: ")

for i in range(11):
	print(sentence[i], end='')

print('\n')

print(sentence[0:11])
print(sentence[slice(0,11)])

# task. display everything except last ten chars

print(sentence[:-10])
	