#Exercise 5-10 Checking Usernames
current_users = ['claudia', 'vinicius', 'miguel', 'valdson', 'admin']
new_users = ['betania', 'everton', 'CLAUDIA', 'ozzy', 'vinicius']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('The person will need to enter a username other than:', new_user)
    else:
        print('The username', new_user, 'is available.')
