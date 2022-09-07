# find minimum number from array
# learn differences between arrays, lists and tuples in Python

import array as arr

a = arr.array('i', [])

for i in range(5):
	a.append(int(input('Enter a number: ')))

for p in a:
	print(p,end=' ')

m = a[0]

for j in range(5):
	if (a[j]) < m:
		m = a[j]
print('\n', m)
