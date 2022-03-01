#Changing dinner guest list
guests = ['thiago', 'ricardo', 'rodolfo']
print('Dinner guest list')
print('-' * 50)
print(guests[0].title(), '- Answered the invitation.')
print(guests[1].title(), '- Invitation sent.')
print(guests[2].title(), '- Invitation sent.')
#Removing Thiago from the list
dropout_guests = guests.pop(0)
print('-' * 50)
print(dropout_guests.title(), 'will not be able to attend the dinner.')
#Adding new guest to the list.
guests.append('vinicius')
print('-' * 50)
#New full dinner guest list
print('New dinner guest list')
print('-' * 50)
print(guests[0].title(), '- Invitation sent.')
print(guests[1].title(), '- Invitation sent.')
print('Hello', guests[2].title() + ",", 'I would like to invite you to dinner next weekend at my beach house.')
