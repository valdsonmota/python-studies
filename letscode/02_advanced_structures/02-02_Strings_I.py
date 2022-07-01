empresa = 'Google'
print(empresa)

empresa = "Google"
print(empresa)

#empresa = 'Let's Code'

empresa = "Let's Code"
print(empresa)

frase = "O professor Pietro da Let's Code disse: \"Hoje pago uma pizza\""
print(frase)

empresa = 'Google'
print(empresa[0])
print(empresa[:3])

nomes_cidades = 'são paulo, belo horizonte, rio de janeiro, brasília'
nomes_cidades = nomes_cidades.split(', ')

cabecalho = '          MENU PRINCIPAL          '
print(cabecalho.strip())

nome_cidade = 'rIo DE jaNeirO'

print(nome_cidade.title())
print(nome_cidade.capitalize())
print(nome_cidade.lower())
print(nome_cidade.upper())

nome_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhora?')
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'rio de janeiro':
    print('Tente novamente!')
    nome_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhora?')

    print('Resposta correta!')

mensagem = 'Você viu o que o Pietro disse na sala de aula ontem?'
fui_citado = 'Pietro' in mensagem
print(fui_citado)
