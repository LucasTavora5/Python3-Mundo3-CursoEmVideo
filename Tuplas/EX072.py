'''Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco'
        , 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
        'Dezesseis', 'DEzessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
    else:
        print('Número fora do intervalo permitido. Tente novamente!')
        continue
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar != 'S':
        break
print('Fim do programa!!')