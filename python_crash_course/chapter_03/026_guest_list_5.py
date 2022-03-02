#Shrinking the guest list
guests = ['vinicius', 'miguel']
print('>' * 18, 'CANCELLATION', '<' * 18)
print('')
print('Dear guests', guests[0].title(), 'and', guests[1].title() + '!' + '\n\nDinner was completely cancelled.')
print('-' * 50)
del guests[0]
del guests[0]
print('All invites cancelled.')
print('-' * 50)
print(guests) #Full list
