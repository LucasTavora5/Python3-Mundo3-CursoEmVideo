''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
expressao = input("Digite uma expressão com parênteses: ")

# Inicializa uma pilha para rastrear os parênteses
pilha = []

# Verifica cada caractere na expressão
for caractere in expressao:
    if caractere == '(':
        # Se encontrar um parêntese de abertura, adiciona à pilha
        pilha.append(caractere)
    elif caractere == ')':
        # Se encontrar um parêntese de fechamento, verifica se há um correspondente aberto
        if not pilha:
            print("Expressão inválida! Parênteses não estão balanceados.")
            break
        pilha.pop()  # Remove o parêntese de abertura correspondente

# Verifica se a pilha está vazia no final
if not pilha:
    print("Expressão válida! Parênteses estão balanceados.")
else:
    print("Expressão inválida! Parênteses não estão balanceados.")