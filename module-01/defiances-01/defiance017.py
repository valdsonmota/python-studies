#Program that reads the length of the opposite and adjacent sides of a right triangle, calculates and displays the length of the hypotenuse.
import math
print('=' * 10, 'DEFIANCE 017', '=' * 10)
opo = float(input('Opposite leg length: '))
adj = float(input('Adjacent side length: '))
hip = math.hypot(opo, adj)
print('The hypotenuse will measure {:.2f}'.format(hip))
