# display numbers divisible by 3 from a list

num_list = []

for i in range(10):
	num_list.append(int(input("Enter a number: ")))

for i in num_list:
	if i % 3 == 0 and i % 5 == 0:
		print(i, end=' ')

print("\n The above are divisible by 3 and 5 from the list")

