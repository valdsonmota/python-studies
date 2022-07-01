dados_cidade = {
    'nome': 'Maceió',
    'estado': 'Alagoas',
    'area_km2': 510,
    'populacao_milhoes': 1025,
}

print(type(dados_cidade))

print(dados_cidade)

dados_cidade['pais'] = 'Brasil'
print(dados_cidade)

print(dados_cidade['nome'])

dados_cidade['area_km2'] = 509
print(dados_cidade)

dados_cidade_2 = dados_cidade
dados_cidade_2['nome'] = 'Garanhuns'
print(dados_cidade_2)
print(dados_cidade)

dados_cidade_3 = dados_cidade.copy()
dados_cidade_3['estado'] = 'Pernambuco'
print(dados_cidade)

novos_dados = {
    'populacao_milhoes': 15,
    'fundacao': '25/01/1554'
}

dados_cidade.update(novos_dados)
print(dados_cidade)

print(dados_cidade.get('prefeito'))

#Retorna uma lista de chaves de um dicionário
print(dados_cidade.keys())
print('')
#Retorna uma lista de valores de um dicionário
print(dados_cidade.values())
print('')
#Retorna uma lista de tuplas (chave, valor) de um dicionário
print(dados_cidade.items())
print('')
