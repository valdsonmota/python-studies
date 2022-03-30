#Exercise 7-2 Restaurant Seating
question = input('How many people are in your dinner group? ')
answer = int(question)
if answer > 8:
    print('You will have to wait for a table.')
else:
    print('Your table is ready, follow me.')
