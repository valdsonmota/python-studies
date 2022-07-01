#LISTAS
nomes_paises = ['brasil', 'argentina', 'china', 'canadá', 'japão']
print(nomes_paises)
print('Tamanho da lista:', len(nomes_paises))
print('País:', nomes_paises[4])
print('País:', nomes_paises[-1])

nomes_paises[4] = 'colômbia'
print('País:', nomes_paises[4])
print(nomes_paises)
print(nomes_paises[1:3])
print(nomes_paises[1:-1])
print(nomes_paises[2:])
print(nomes_paises[:3])
print(nomes_paises[:])
print(nomes_paises[::2])
print(nomes_paises[::-1])
print("brasil" in nomes_paises)
print("canadá" not in nomes_paises)

lista_capitais = []
lista_capitais.append('brasilia')
lista_capitais.append('buenos aires')
lista_capitais.append('pequim')
lista_capitais.append('bogotá')
print(lista_capitais)

lista_capitais.insert(2, 'paris')
print(lista_capitais)

lista_capitais.remove('buenos aires')
print(lista_capitais)

removido = lista_capitais.pop(2)
print(lista_capitais, removido)

#TUPLAS
paises = ('brasil', 'argentina', 'china', 'canadá', 'japão')
print(paises, type(paises))

nome_estado = 'são paulo',
print(nome_estado, type(nome_estado))
len(paises)
paises[0]

b, a, c, ca, j = paises
print(b, c, j)

print(*paises)
