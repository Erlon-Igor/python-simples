from random import randint

numero_maquina = randint(1, 50)

try:
    tentativa = 1
    numero_usuario = int(input('\nAdivinhe um número entre 1 e 50: '))
    while numero_usuario != numero_maquina:
        if numero_maquina > numero_usuario:
            print(f'Errou o número é maior que {numero_usuario}')
        else:
            print(f'Errou o número é menor que {numero_usuario}')
        numero_usuario = int(input('Tente novamente: '))
        tentativa += 1

    print(f'Correto!!!\nNúmero da máquina: {numero_maquina}\nNúmero do jogador: {numero_usuario}')
    print(f'Tentativas: {tentativa}\n')
except Exception as erro:
    print('\nAlgo de errado aconteceu!')
    print(f'Erro: {erro}\n')
