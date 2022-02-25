#Program to read any angle and show the value of the sine, cosine and tangent of that angle on the screen.
from math import radians, sin, cos, tan
print('=' * 10, 'DEFIANCE 018', '=' * 10)
ang = float(input('Enter the desired angle: '))
sn = sin(radians(ang))
cs = cos(radians(ang))
tn = tan(radians(ang))
print('The angle {} has the sine of: {:.2f}'.format(ang, sn))
print('The angle {} has the cosine of: {:.2f}'.format(ang, cs))
print('The angle {} has the tangent of: {:.2f}'.format(ang, tn))
