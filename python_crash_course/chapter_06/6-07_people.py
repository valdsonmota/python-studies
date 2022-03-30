#Exercise 6-7 People
person_0 = {
    'first_name': 'claudia',
    'last_name': 'santos',
    'age': 35,
    'city': 'maceio'
    }
person_1 = {
    'first_name': 'vinicius',
    'last_name': 'alves',
    'age': 25,
    'city': 'maceio'
    }
person_2 = {
    'first_name': 'valdson',
    'last_name': 'mota',
    'age': 40,
    'city': 'maceio'
    }
people = [person_0, person_1, person_2]
for person in people:
    full_name = person['first_name'] + ' ' + person['last_name']
    age = person['age']
    city = person['city']
    print(
        '\nFull name:', full_name.title(),
        '\nAge:', age,
        '\nCity:', city.title()
    )
