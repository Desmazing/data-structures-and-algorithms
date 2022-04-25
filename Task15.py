lst = []
for i in range(6):
	num = int(input('Enter a number: '))
	lst.append(num)

tpl = tuple(lst)
print(tpl)

lst.clear()
print(tuple(lst))