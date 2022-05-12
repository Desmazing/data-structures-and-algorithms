# find middle element of list items
import math

lst = [1,2,4,16,2,6,7]

a = len(lst)
print(f'List length is {a}')

b = a/2

print(f'Mid element is {lst[int(b)]}')
print(f'Square root of mid element is {math.sqrt(lst[int(b)])}')