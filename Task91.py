# find mass from density
# mass = volume * density

density = float(input("Enter object density in g/cm3: "))
volume = float(input("Enter object volume in cm3: "))

mass = density * volume

print(f'Object mass is {mass} grams')