#Exercise 7-3 Multiples of Ten
enter = input('Enter a number: ')
number = int(enter)
if number % 10 == 0:
    print(
        enter,
        'is a multiple of ten.'
    )
else:
    print(
        enter,
        'is not a multiple of ten.'
    )
