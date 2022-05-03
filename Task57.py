# make binary to decimal calculator

bin = input('Enter your binary number here: ')
bin_lst = []
for bit in bin:
	bin_lst.append(bit)

print(bin_lst)	
bin_lst.reverse()
print(bin_lst)

dec = 0
mul = 0
for i in bin_lst:
	if i == '0':
		dec = dec + 0
		mul += 1
	elif i == '1':
		dec = dec + (2 ** mul)
		mul += 1
		

print(dec)
		

