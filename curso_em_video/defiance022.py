# Program reads a person's full name and displays:
# > The name in all UPPERCASE
# > The name in all lowercase
# > How many letters in total (not including spaces)
# > How many letters are in the first name?
print('=' * 10, 'DEFIANCE 022', '=' * 10)
nom = str(input('Enter a full name: '))
div = nom.split()
jun = ''.join(div)
print('Name in UPPERCASE: {}'.format(nom.upper()))
print('Name in lowercase: {}'.format(nom.lower()))
print('The name has {} letters in all'.format(len(jun)))
print('The first name has {} letters'.format(len(div[0])))
