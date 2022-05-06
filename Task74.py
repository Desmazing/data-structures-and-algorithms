# get student marks
# get student names
# find second position of student in a list
# display student marks and student name

student_marks = {}

for i in range(3):
	name = input("Enter student name: ")
	marks = int(input("What did the student score? "))
	student_marks[name] = marks

print(student_marks)

# lets find second highest mark

mark2 = list(student_marks.values())
print(mark2)
mark2.sort(reverse = True)
print(mark2)

# lets find the matching key, value pair in the dictionary

for name in student_marks.keys():
	if student_marks[name] == mark2[1]:
		print(f'{name} scored {mark2[1]})