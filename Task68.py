# get list
# display in descending order

lst = []

for i in range(6):
	lst.append(int(input("Enter your student id here: ")))

lst.sort(reverse = True) # sorts a list in descending order
print(lst)

# this is where the assignment begins

lst.clear()
print(lst)