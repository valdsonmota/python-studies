#Exercise 6-6 Polling
people = [
    'claudia',
    'vinicius',
    'michel',
    'valdson',
    'ozzy'
    ]
polling = {
    'claudia': 'python',
    'vinicius': 'qlik sense',
    'valdson': 'python'
}
print(
    '-' * 10,
    'POLLING',
    '-' * 10
)
for person in people:
    if person in polling:
        print(
            '\n' + person.title(),
            'thanks for answering the poll.'
        )
    else:
        print(
            '\n' + person.title() +
            ': Please answer the poll.'
        )
