# 6 marks input from user...
# calculate total, average and percentage

subj1 = int(input('Enter 1st subject mark: '))
subj2 = int(input('Enter 2nd subject mark: '))
subj3 = int(input('Enter 3rd subject mark: '))
subj4 = int(input('Enter 4th subject mark: '))
subj5 = int(input('Enter 5th subject mark: '))
subj6 = int(input('Enter 6th subject mark: '))

total = subj1 + subj2 + subj3 + subj4 + subj5 + subj6
average = total / 6
percentage = ((average/100) * 100) 

print('\nYour total mark is: '+str(total))
print('Your average mark is: '+str(average))
print('Your percentage is: '+str(percentage)+ ' %')
