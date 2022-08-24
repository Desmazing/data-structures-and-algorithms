# display numbers in reverse order

s = int(input("Enter a starting number: "))
e = int(input("Enter an ending number: "))

sum = 0

for i in range(s, e-1, -1):
	print(i)
	sum += i
print(f"Sum is {sum}")
	
