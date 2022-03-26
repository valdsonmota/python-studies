#Exercise 5-9 Hello Admin 
users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello', user.title() + ',', 'Welcome Dungeon Master.')
        else:
            print('Hello', user.title() + ', thank you for logging in again.')
else:
    print('We need to find some users!')
