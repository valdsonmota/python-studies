#Exercise 6-8 Pets
ozzy = {
    'name': 'ozzy',
    'kind': 'cat',
    'mom': 'claudia'
}
little_black = {
    'name': 'little black',
    'kind': 'dog',
    'mom': 'cristina'
}
pets = [ozzy, little_black]
for pet in pets:
    name = pet['name']
    kind = pet['kind']
    mom = pet['mom']
    print(
        '\nName:', name.title(),
        '\nKind:', kind.title(),
        '\nMom:', mom.title()
    )
