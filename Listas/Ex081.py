'''Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('=-' *30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Lista ordenada de forma decrescente:{lista}')
if 5 in lista:
    print('O valor "5" foi encontrado na lista')
else:
    print('O valor "5" não foi encontrado na lista')

print('=-' *30)
print('PROGRAMA FINALIZADO!!')
print('=-' *30)