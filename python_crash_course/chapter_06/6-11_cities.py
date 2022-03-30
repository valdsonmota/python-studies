#Exercise 6-11 Cities
cities = {
    'brisbane': {
        'country': 'australia',
        'population': '2,28 millions',
        'fact': 'Capital of Queensland, it is a large city on the banks of the Brisbane River'
    },
    'gold coast': {
        'country': 'australia',
        'population': '540 thousand',
        'fact': 'A metropolitan region south of Brisbane on the east coast of Australia.'
    },
    'vancouver': {
        'country': 'canada',
        'population': '675 thousand',
        'fact': "A bustling port city on British Columbia's west coast, it is among Canada's densest and most ethnically diverse cities."
    }
}
for city, information in cities.items():
    print(
        '\n' + city.title() + ':'
    )
    for info, description in information.items():
        print(
            '\t' + info.title() + ':',
            description.title()
        )
