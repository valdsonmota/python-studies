nomes_cidades = ['Maceió', 'Brisbane', 'Vancouver', 'New York']
for cidade in nomes_cidades:
    print(cidade)

nomes_cidades = 'Maceió', 'Brisbane', 'Vancouver', 'New York'
for cidade in nomes_cidades:
    print(cidade)

dados_cidade = {
    'nome': 'Maceió',
    'estado': 'Alagoas',
    'populacao_milhoes': 1.5
}
for chave in dados_cidade:
    print(f'{chave}: {dados_cidade[chave]}')

nomes_cidades = ['Maceió', 'Brisbane', 'Vancouver', 'New York']
for nome in nomes_cidades:
    nome = 'Rio de Janeiro'
print(nomes_cidades)

for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = 'Garanhuns'
print(nomes_cidades)

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))