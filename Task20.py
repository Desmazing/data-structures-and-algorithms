# array will have same data type

import array as arr

a = arr.array('i', [])

for i in range(5):
	a.append(int(input('Enter number here: ')))

#s = 0
#for j in range(5):
#	print(a[j])
#	s += a[j]

maxx = max(a)
print('Max in array numbers is '+str(maxx))
