#The program receives the name of four students and chooses one of them.
from random import choice
print('=' * 10, 'DEFIANCE 019', '=' * 10)
list = input('Enter the name of the first student: '), \
        input('Enter the name of the second student: '), \
        input('Enter the name of the third student: '), \
        input('Enter the name of the fourth student: ')
choose = choice(list)
print('-+' * 35)
print('The participating students are: ', list)
print('-+' * 35)
print('The chosen student was: ', '>' * 5, choose, '<' * 5)
print('-+' * 25)
