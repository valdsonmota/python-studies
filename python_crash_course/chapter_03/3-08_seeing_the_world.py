#Exercise 3-8 - Seeing the World
cities = ['bariloche', 'machu picchu', 'auckland', 'lisboa', 'madrid', 'paris', 'bruxelas', 'londres', 'dublin', 'toronto']
#List in original order
print('List in original order')
print(cities)
print('-' * 115)
#Temporary alphabetical order list.
print('Alphabetical order without changing the original list')
print(sorted(cities))
print('-' * 115)
#Temporary reverse alphabetical order list.
print('Reverse alphabetical order without changing the original list')
print(sorted(cities, reverse=True))
print('-' * 115)
#List in original order
print('List in original order')
print(cities)
print('-' * 115)
#Invertive original list
print('Invertive original list')
cities.reverse()
print(cities)
print('-' * 115)
#Reversing the original list again.
print('Reversing the original list again.')
cities.reverse()
print(cities)
print('-' * 115)
#List in alphabetical order permanently.
print('List in alphabetical order permanently.')
cities.sort()
print(cities)
