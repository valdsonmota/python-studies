#Shrinking the guest list
guests = ['ricardo', 'rodolfo', 'vinicius', 'jailson', 'miguel', 'raphael']
print('>' * 21, 'NOTICE', '<' * 21)
print('')
print('Dear guests', guests[0].title() + ',', guests[1].title() + ',', guests[2].title() + ',', guests[3].title() + ',', guests[4].title(), 'and', guests[5].title() + '!' + '\n\nDue to a problem with the custom furniture factory, I will have to reduce the list to just two guests. My apologies!')
print('-' * 50)
invitation_canceled = guests.pop(0)
print('Sorry', invitation_canceled.title() + ',', 'your invitation has been cancelled.')
invitation_canceled = guests.pop(0)
print('Sorry', invitation_canceled.title() + ',', 'your invitation has been cancelled.')
invitation_canceled = guests.pop(1)
print('Sorry', invitation_canceled.title() + ',', 'your invitation has been cancelled.')
invitation_canceled = guests.pop(2)
print('Sorry', invitation_canceled.title() + ',', 'your invitation has been cancelled.')
print('-' * 50)
print('Update dinner guest list')
print('-' * 50)
print('Hi', guests[0].title() + ',', 'your invitation remains confirmed.')
print('Hi', guests[1].title() + ',', 'your invitation remains confirmed.')
print('-' * 50)
print(guests) #Full list
