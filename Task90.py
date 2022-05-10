# get age of 5 students
# store in a list
# display ages between 14 and 20

ages = []

for i in range(5):
	ages.append(int(input("Enter the age here: ")))

print(ages)

for age in ages:
	if 14<age<20:
		print(age)

# get names of students
# store in list
# store student name starting at 'a' and ending at 'a'

names = []
for i in range(5):
	names.append(input("Enter student names: "))

for name in names:
	if name.startswith('a') and name.endswith('a'):
		print(name)

