# area

b = float(input('Enter base of triangle: '))
h = float(input('Enter height of triangle: '))

triangle_area = (b * h)/2

print(f'Area of your triangle is {triangle_area}')
num = float(input('\nNow enter a number: '))
new_num = triangle_area + num

print(f'Addition of number with triangle area is {new_num}')