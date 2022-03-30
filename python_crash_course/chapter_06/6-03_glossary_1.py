#Exercise 6-3 Glossary
glossary = {
    'list': 'A list is a collection of items in a particular order.',
    'range': "Python's range() function makes it easy to generate a series of numbers",
    'tuple': 'In Python, tuples are very similar to lists, however, unlike lists, they are immutable.',
    'for': 'A for loop acts like an iterator in Python, it goes through items that are in a sequence or any other iterable item.',
    'if': 'If in Python allows us to tell the computer to perform alternative actions based on a given result set.'
    }
print('-' * 10, 'GLOSSARY', '-' * 10)
for key, values in glossary.items():
    print(
        key.title() + ':',
        '\n\t' + values + '\n'
    )
