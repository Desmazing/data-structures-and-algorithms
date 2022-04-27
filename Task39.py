# pass keyword is a placeholder in python functions, doesn't bring an error


lst = []

for i in range(5):
	lst.append(int(input('Enter a number: ')))
tpl = tuple(lst)
print(tpl)

def addmul(tpl):
	s = 0
	m = 1
	for j in tpl:
		s += j
		m *= j
	print(f'Addition is {s}')
	print(f'Multiplication is {m}')

addmul(tpl)