#Exercise 6-5 Rivers 1
rivers = {
    'san francisco': 'brazil',
    'amazonas': 'brazil',
    'parana': 'brazil'
}
for river, about in rivers.items():
    print('\n',
            river.title(),
            'River crosses',
            about.title())
