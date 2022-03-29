#Exercise 6-5 Rivers 2
rivers = {
    'san francisco': 'also known as old Chico',
    'amazonas': 'the largest Brazilian river.',
    'parana': 'the eighth longest river in the world by length.'
}
for river, about in rivers.items():
    print('\n',
            river.title(),
            'River is',
            about)
