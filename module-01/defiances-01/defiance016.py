#Program that reads any Real number from the keyboard and displays its entire portion on the screen.
print('=' * 10, 'DEFIANCE 016', '=' * 10)
num = float(input('Enter a real number: '))
print('The number {} has its integer portion {}'.format(num, int(num)))