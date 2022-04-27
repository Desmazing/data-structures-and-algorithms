# get angle
# find cos and sin in rad

import math

angle = float(input('Enter the angle: '))

sinval = math.sin(angle)
cosval = math.cos(angle)

print(f'sin is {sinval}')
print(f'cos is {cosval}')

deg_angle = math.degrees(angle)
print(deg_angle)
