# find acceleration of object

vi = float(input("Enter intial velocity in m/s: "))
vf = float(input("Enter final velocity in m/s: "))
acc = float(input("Enter acceleration in m/s2: "))

vel_change = vf - vi
t = vel_change / acc

print(f"Time taken by object is {t} s")