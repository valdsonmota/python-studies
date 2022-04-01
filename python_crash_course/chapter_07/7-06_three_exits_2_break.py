#Exercise 7-6 Three Exits 2 - Break
print(
    '\nEnter your age.',
    '\nFor go out program, enter finish.'
)
while True:
    age = input('Age: ')
    if age == 'finish':
        break
    else:
        age_int = int(age)
        if (age_int < 3) and (age_int >= 0):
            print(
                '\nYour ticket is free.\n'
            )
        elif (age_int >= 3) and (age_int <= 12):
            print(
                '\nYour ticker costs $10.\n'
            )
        elif (age_int > 12) and (age_int <= 122):
            print(
                '\nYour ticket costs $15.\n'
            )
        elif (age_int < 0) or (age_int > 122):
            print(
                '\nYou are not alive!\n'
            )
print(
    '\nProgram fnished.\n'
)