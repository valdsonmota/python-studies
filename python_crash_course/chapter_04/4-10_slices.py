#Exercise 4-10 - Slices
slices = [slice for slice in range(1,21)]
print('Full list\n', slices)
print('\nThe first three numbers on the list are:\n', slices[:3])
print('\nThe three numbers in the middle of the list are:\n', slices[8:11])
print('\nThe last three numbers on the list are:\n', slices[-3:])
