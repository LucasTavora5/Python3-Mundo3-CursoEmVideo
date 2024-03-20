temp = []
princ = []
mai = men = 0
#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#início da leitura dos nomes e pesos
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    #listando pesos
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    #fim da leitura de nomes e pesos
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
#A) Quantas pessoas foram cadastradas.
print(f'Você cadastrou {len(princ)} pessoas!')
#B) Uma listagem com as pessoas mais pesadas.
print(f'O maior peso foi de {mai}Kg.', end='')
#listando e relacionando pessoa ao peso
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]')
#C) Uma listagem com as pessoas mais leves.
print(f'O menor peso foi de {men}Kg.', end='')
#listando e relacionando pessoa ao peso
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]')

'''temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Ao todo você cadastrou {len(princ)}pessoas')
print(f'O maior peso foi de {mai}Kg', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {men}Kg')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')'''


