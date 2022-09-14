# Take two numbers and operator -- return result
# must be refactored

operator_list = ['+','-','*','/','%','//']


def arithmeticOps():
	a = int(input('Enter first number: '))
	b = int(input('Enter second number: '))
	op = input('Enter operator: ')

	if op in operator_list:
		if op == '+': result = a + b; print('Addition is:',result)
		elif op == '-': result = a - b; print('Subtraction is:',result)
		elif op == '*': result = a * b; print('Multiplication is:',result)
		elif op == '/': result = a / b; print('Division is:',result)
		elif op == '%': result = a % b; print('Modulus is:',result)
		elif op == '//': result = a // b; print('Floor is:',result)
	else:
		print('invalid operator inputs. Try again')
		arithmeticOps()

arithmeticOps()
