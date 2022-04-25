lst = []
for i in range(6):
	num1 = int(input('Enter number: '))
	lst.append(num1)

print(lst)
tpl = tuple(lst)
print(tpl)

sum = 0
for i in tpl:
	sum += i

print(sum)
