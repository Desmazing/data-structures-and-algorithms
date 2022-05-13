# add numbers from a list
# should be greater than 5 and less than 10
# Task is to add only even numbers from a list

lst = [1,5,7,13,124,765,123,1,9,8,5,6,6,8,7,234,234,2,1]

sum1 = 0
even_sum = 0

for num in lst:
	if 5<num <10:
		sum1 += num

print(f'Sum of the numbers is {sum1}')

for num in lst:
	if num % 2 == 0:
		even_sum += num

print(f'Sum of even numbers in list is {even_sum}')