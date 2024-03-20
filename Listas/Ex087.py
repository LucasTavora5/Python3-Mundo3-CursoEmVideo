#Aprimore o desafio anterior, mostrando no final:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna = segunda_linha = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Insira os valores para [{l},{c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        # A) A soma de todos os valores pares digitados.
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print(f'A soma dos pares é: {soma_par}')
# B) A soma dos valores da terceira coluna.
for l in range(0,3):
    soma_coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é:{soma_coluna}')
# C) O maior valor da segunda linha.
for c in range(0,3):
    if c == 0:
        segunda_linha = matriz[1][c]
    elif matriz[1][c] > segunda_linha:
        segunda_linha = matriz[1][c]
print(f'O maior elemento da segunda linha é: {segunda_linha}')