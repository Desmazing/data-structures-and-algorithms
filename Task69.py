# create file
# get name and age
# write on the file

file = open('name_file.txt', 'w+')
name = input("Enter your name: ")
age = int(input("Enter your age: "))
file.write(name)
file.write('\nYour age is '+str(age))
file.close()

file = open('name_file.txt', 'r')
print(file.read()) # display to stand output
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
reslt = num1 + num2
file.close()

file = open('name_file.txt', 'a+')
file.write(f'\nSum of {num1} and {num2} is {reslt}')
file.close()

