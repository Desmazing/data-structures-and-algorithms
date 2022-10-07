# take user number input
# determine whether odd or even

num1 =  int(input('Enter a number: '))

if num1 % 2 == 0: print('Even number.');
else: print('Odd number.')
print(f'Square of {num1} is {num1 * num1}')

def odd_even(num1):
  return "Odd number." if num1%2 else "Even number."
