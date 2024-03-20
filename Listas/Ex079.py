'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado!')
    else:
        print('Valor duplicado, insira novamente!')
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
print('=-' *30)
print(f'Você inseriu os valores:{numeros}')
print('=-' *30)
print('PROGRAMA FINALIZADO!!')
print('=-' *30)