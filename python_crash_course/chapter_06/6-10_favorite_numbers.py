#Exercise 6-10 Favorite Numbers
favorite_numbers = {
    'claudia': [
        1, 10, 11, 20, 21, 30
    ],
    'vinicius': [
        2, 9, 12, 19, 22, 81
    ],
    'miguel': [
        3, 8, 13, 18, 23, 21
    ],
    'valdson': [
        9, 10, 27, 30, 32, 37
    ],
    'ozzy': [
        5, 6, 15, 16, 19, 25
    ]
    }
print('-' * 8, 'FAVORITE NUMBERS', '-' * 8)
for name, number in favorite_numbers.items():
    print(
        name.title() +
        "'s favorite number are:",
        str(number) + '.'
    )
