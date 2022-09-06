# get 5 subject marks from user, store them in array, student name.
# Find total and display each subject marks
# simple algorithms to explore basics

import array as arr

marks_arr = arr.array('i', [])
subj_list = ['English', 'Math', 'AI', 'Physics', 'Computer']
total = 0

name = input("Enter your name here: ")
print(f'Hello {name}!\n')

for subject in subj_list:
	marks_arr.append(int(input(f"Enter your {subject} mark: ")))

for mark in marks_arr:
	total += mark

print(f'Your total mark is {total}.\nHere is a breakdown:')

ind = 0

for subj in subj_list:
	print(f'\t{subj} = {marks_arr[ind]}')
	ind += 1

print(f'Your average mark is {total/5}')



