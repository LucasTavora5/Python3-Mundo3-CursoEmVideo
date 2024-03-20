'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
# Tupla com nomes de produtos e preços
listagem = ('Lápis', 1.75,
            'Borracha', 1.00,
            'Caderno',20.00,
            'Caneta',5.00,
            'Estejo', 9.00,
            'Mochila', 120.00,
            'Livros', 50.00)
print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)
for pos in range(0,len(listagem)):
    if pos %2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>2}')