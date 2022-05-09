# print first and last chars from a string

entry = input("Enter string here: ")

print('first char is ', entry[0])
print('last char is', entry[-1])

# remove first and last char from string
# could use replace method

a = entry.replace(entry[0], '', 1) # returns string copy without first index
b = a.replace(a[-1], '', 1)

print(b)
print(entry)