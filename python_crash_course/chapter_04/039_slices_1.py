#Code with a list from 1 to 20, uses slices to display the first three numbers in the list, the three numbers in the middle of the list, and the last three numbers in the list.
slices = [slice for slice in range(1,21)]
print('Full list\n', slices)
print('\nThe first three numbers on the list are:\n', slices[:3])
print('\nThe three numbers in the middle of the list are:\n', slices[8:11])
print('\nThe last three numbers on the list are:\n', slices[-3:])
