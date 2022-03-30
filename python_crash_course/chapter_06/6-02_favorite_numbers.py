#Exercise 6-2 Favorite Numbers
favorite_numbers = {
    'claudia': 30,
    'vinicius': 81,
    'miguel': 21,
    'valdson': 27,
    'ozzy': 19
    }
print('-' * 8, 'FAVORITE NUMBERS', '-' * 8)
for name, number in favorite_numbers.items():
    print(
        name.title() +
        "'s favorite number is",
        str(number) + '.'
    )
