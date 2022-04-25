passmark = 60

name = input('Enter your name:')
marks = float(input('Enter your marks: '))

if 0< marks < passmark:
    print('Sorry '+name+', you cannot be admitted. You need '+str(passmark-marks)+' more points')
else:
    print('Congrats! Proceed to admission')
