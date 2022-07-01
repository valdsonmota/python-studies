cumprimento = 'Olá, '
nome = 'Valdson'
print(cumprimento + nome)

print(nome * 5)

nome = 'Valdson Mota'
idade = 40
n_filhos = 0
print(nome + ' tem ' + str(idade + ' anos e ' + str(n_filhos) + ' filhos.'))

print('{} tem {} anos e {} filhos.'.format(nome, idade, n_filhos))

preco_gasolina = 7.488
print('O preço da gasolina hoje em Maceió-AL está de R$ {:.2f}'.format(preco_gasolina))

print(f'{nome} tem {idade} anos e {n_filhos} filhos.')
