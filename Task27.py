# check whether year is leap
# get 5 years from a user
# store in an array
# return only the leap years

import array as arr
# what does the array module do?

year_arr = arr.array('i', [])

for i in range(5):
	year_arr.append(int(input('Enter a year: ')))


for j in range(5):
	if (year_arr[j]) % 4 == 0:
		print(year_arr[j], end=' ') 

