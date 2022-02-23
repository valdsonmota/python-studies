#Program that chooses the order of presentation among four students.
from random import shuffle
print('=' * 10, 'DEFIANCE 020', '=' * 10)
s1 = input('Enter the name of the first student: ')
s2 = input('Enter the name of the second student: ')
s3 = input('Enter the name of the third student: ')
s4 = input('Enter the name of the fourth student: ')
list = [s1, s2, s3, s4]
print('-' * 70)
print('The participating students are: {}'.format(list))
shuffle(list)
print('-' * 70)
print('')
print('>' * 70)
print('The order of presentation will be: {}'.format(list))
print('>' * 70)
