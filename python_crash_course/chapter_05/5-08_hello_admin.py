#Exercise 5-8 Hello Admin
users = ['claudia', 'vinicius', 'miguel', 'valdson', 'admin']
for user in users:
    if user == 'admin':
        print('Hello', user.title() + ',', 'Welcome Dungeon Master.')
    else:
        print('Hello', user.title() + ', thank you for logging in again.')
