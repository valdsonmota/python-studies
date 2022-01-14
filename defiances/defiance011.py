#Program that reads the width and height of a wall in meters, calculates the area and amount of paint you need, knowing that each liter of paint paints an area of 2m².
print('=' * 10, 'DEFIANCE 011', '=' * 10)
hei = float(input('Enter the height of the wall in meters: '))
wid = float(input('Enter the width of the wall in meters: '))
sm = hei * wid
pai = sm / 2
print('The wall is {}m², you will need {:.1f} liters of paint.'.format(sm, pai))
