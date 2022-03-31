#Exercise 7-5 Movie Tickets
print('\nEnter your age.')
print('For go out program, enter finish.')
age = ''
while age != 'finish':
    age = input('Age: ')
    if age != 'finish':
        age_int = int(age)
        if (age_int < 3) and (age_int >= 0):
            print('\nYour ticket is free.\n')
        elif (age_int >= 3) and (age_int <= 12):
            print('\nYour ticker costs $10.\n')
        elif (age_int > 12) and (age_int <= 122):
            print('\nYour ticket costs $15.\n')
        elif (age_int < 0) or (age_int > 122):
            print('\nYou are not alive!\n')
    else:
        print('\nProgram fnished.\n')
