#Exercise 6-9 Favorite Places
favorite_places = {
    'claudia': [
        'maceio',
        'gold coast',
        'melbourne',
        'new york'
    ],
    'vinicius': [
        'maceio'
    ],
    'valdson': [
        'gold coast',
        'brisbane',
        'vancouver',
        'new york'
    ]
}
print('-' * 10, 'FAVORITE PLACES', '-' * 10)
for person, places in favorite_places.items():
    if len(places) > 1:
        print(
            '\n' + person.title() +
            "'s favorite places are:"
        )
        for city in places:
            print(
                '\t' + city.title()
            )
    else:
        print(
            '\n' + person.title() +
            "'s favorite places is:"
        )
        for city in places:
            print(
                '\t' + city.title()
            )
