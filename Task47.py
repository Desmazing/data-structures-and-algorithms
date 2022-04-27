import math

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

sq1 = math.pow(num1, 3)
sq2 = math.pow(num2, 3)

tot = sq1 + sq2
print(f'\nThe result is {tot}')