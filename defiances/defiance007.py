#Program that reads the two points of a student, calculates and displays their average.
print('====== DEFIANCE 007 ======')
nam = input('Enter student name: ')
po1 = float(input('Enter the first point: '))
po2 = float(input('Enter the second point: '))
avg = (po1 + po2) / 2
print('The student average {} between {:.1f} and {:.1f} is: {:.1f}'.format(nam, po1, po2, avg))
