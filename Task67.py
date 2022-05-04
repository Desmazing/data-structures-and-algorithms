# sum of two numbers
# 1st is positive
# 2nd is negative

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if 20<num1<50 and num2 < 0:
	result = num1 + num2
	print(result)
else:
	print("1st number must be between 20 and 50. 2nd must be negative")