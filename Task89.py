# generate even numbers from 0 to 20
# generate odd numbers from 0 to 20
# add both and display

even_sum = 0
odd_sum = 0

for i in range(0, 21):
	if i % 2 == 0:
		print(i, end=' ')
		even_sum += i
print('\n')

for i in range(0, 20):
	if i % 2 != 0:
		print(i, end=' ')
		odd_sum += i
print('\n')
print(f'Even sum is {even_sum}')
print(f'Odd sum is {odd_sum}')
print(f'Total sum is {even_sum + odd_sum}\n')

# generate numbers div by 3 from 0 to 20
# generate numbers div by 5 from 0 to 20
# add both and display

three_sum = 0
five_sum = 0

for i in range(0, 21):
	if i % 3 == 0:
		print(i, end=' ')
		three_sum += i

print('\n')

for i in range(0, 21):
	if i % 5 == 0:
		print(i, end=' ')
		five_sum += i

print('\n')
print(f'Three sum is {three_sum}')
print(f'Five sum is {five_sum}')
print(f'Total sum is {three_sum + five_sum}')