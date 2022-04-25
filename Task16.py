num = int(input('Enter number here: '))
lst = []

num += 5
print(num)
lst.append(num)
num -= 5
lst.append(num)
print(num)
num *= 5
lst.append(num)
print(num)
num /= 5
lst.append(num)
print(num)
num %= 5
lst.append(num)
print(num)

a = 0
for i in lst:
	a += i
print(a)