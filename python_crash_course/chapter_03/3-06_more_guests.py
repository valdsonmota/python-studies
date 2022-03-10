#Exercise 3-6 - More Guests
guests = ['ricardo', 'rodolfo', 'vinicius']
print('Current dinner guest list')
print('-' * 50)
print(guests[0].title(), '- Confirmed')
print(guests[1].title(), '- Confirmed')
print(guests[2].title(), '- Confirmed')
print('-' * 50)
#Adding new guests to the list.
guests.append('jailson')
guests.append('miguel')
guests.append('raphael')
print('Updated dinner guest list.')
print('-' * 50)
print('Hello', guests[3].title() + ',', 'I would like to invite you to dinner next weekend at my beach house.')
print('Hello', guests[4].title() + ',', 'I would like to invite you to dinner next weekend at my beach house.')
print('Hello', guests[5].title() + ',', 'I would like to invite you to dinner next weekend at my beach house.')
print('-' * 50)
print('New dinner guest list')
print('-' * 50)
print(guests) #Full list
