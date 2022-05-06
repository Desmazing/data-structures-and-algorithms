# get a sentence
# count specific words or characters in sentence
# count method takes one argument and it is quite efficient

s = input("Enter a sentence: ")
w_c = input("Enter word to count: ")
p = 'x'

total = s.count(w_c)
print(f'"{w_c}" appears {total} times in the sentence')

# how to replace a string in python
# use the string replace method

print(s.replace('Desmond', 'Kim', 3)) # only replaces 3 instances if Desmond
# returns a copy of string but does not replace original
# s still remains the same