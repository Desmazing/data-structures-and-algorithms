# get temp in centrigade
# convert it to farenheit and kelvin
# Task is to 

ctemp = float(input("Enter temperature in deg centigrade: "))

ftemp = (ctemp * 9/5) + 32
ktemp = ctemp + 273.15

print(f'Temp converted is {ftemp} Deg F')
print(f'Temp converted is {ktemp} Kelvin')