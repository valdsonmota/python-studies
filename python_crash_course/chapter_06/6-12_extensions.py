#Exercise 6-12 Extensions
cities = {
    'maceio': {
        'country': 'brazil',
        'population': '1,025 millions',
        'fact': 'Maceió, is the capital of the state of Alagoas, on the east coast of Brazil.'
    },
    'gunga beach': {
        'country': 'brazil',
        'population': '-',
        'fact': 'Gunga Beach is located 20 miles south of Maceió, Alagoas. It is considered one of the most beautiful beaches in Brazil.'
    },
    'maragogi': {
        'country': 'brazil',
        'population': '33 thousand',
        'fact': 'Maragogi is a resort town on the coast of the Atlantic Ocean in eastern Brazil. It is known for its long beaches like Burgalhau, near the River of Paus.'
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
