# write a decimal to binary converter
# from base 10 to base 2

dec = int(input("Enter a decimal number: "))
	
binary_str = ""

while dec > 0:
	x = dec % 2
	if x == 0:
		binary_str = '0' + binary_str
		dec = dec // 2
	elif x != 0:
		binary_str = '1' + binary_str
		dec = dec // 2

print(binary_str)

		

