''' Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.

Aula Anterior
Voltar para Módulo'''
num = (int(input('Digite um número:')),
        int(input('Digite um número:')),
        int(input('Digite um número:')),
        int(input('Digite um número:')))
print(f'Você inseriu os valores:{num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)}ª posição')
else:
    print('O valor "3" não foi inserido')
print('Valores pares digitados:', end='')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')