#Exercise 5-11 Ordinal Numbers
ordinal_numbers = list(range(1,10))
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(str(ordinal_number) + 'st')
    elif ordinal_number == 2:
        print(str(ordinal_number) + 'nd')
    elif ordinal_number == 3:
        print(str(ordinal_number) + 'rd')
    else:
        print(str(ordinal_number) + 'th')
