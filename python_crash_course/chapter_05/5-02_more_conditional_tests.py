#Exercise 5-2 More Conditional Tests
people = ['claudia', 'vinicius', 'miguel', 'valdson']
for person in people:
    if person == 'claudia':
        print(person.title(), 'is an adult')
    elif person == 'vinicius':
        print(person.title(), 'is an new adult')
    elif person == 'miguel':
        print(person.title(), 'is a baby')
    else:
        print(person.title(), 'is an old adult.')
