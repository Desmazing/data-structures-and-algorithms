# random module provides a shuffle method
# method takes one arg = list

import random

color_code = []

for i in range(5):
	color_code.append(input("Enter a color here: "))

print(color_code)

random.shuffle(color_code) # returns none
print(color_code)

# display list in ascending and descending order

color_code.sort() # return in ascending order
print(color_code)

color_code.sort(reverse = True) # return descending
print(color_code)
