# get user input. Display tables for the inputs

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("You entered "+str(a)+" and "+str(b))

for i in range(1, 11):
    print(str(i)+" * "+str(a)+ " = "+str(i*a))
    print(str(i)+" * "+str(b)+ " = "+str(i*b))