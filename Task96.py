# get float data types from user
# convert to int
# store in list

flt_lst = []
int_lst = []

for i in range(5):
	flt_lst.append(float(input("Enter float variables here: ")))

print(flt_lst)

for j in flt_lst:
	int_lst.append(int(j))

print(int_lst)

