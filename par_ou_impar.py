def calc(num):
    return num % 2

def par_ou_impar(num):
    if calc(num):
        return 'Ímpar'
    else:
        return 'Par'



def main():
    while True:
        try:
            num = int(input('Em que número você está pensando? '))
            resultado = par_ou_impar(num)
            sair = input(f'{num} é um número {resultado}! Tem outro (sim ou nao)? ').strip().lower()

            if sair not in 'sim s não nao n':
                while sair not in 'sim s não nao n':
                    sair = input('Tem outro (sim ou nao)? ').strip().lower()
                    
            if sair in 'não nao n':
                print('Adeus!!!')
                return ''
        except Exception as erro:
            print('\nAlgo de errado aconteceu!')
            print(f'Erro: {erro}')
            print('Tente novamente\n')


main()
