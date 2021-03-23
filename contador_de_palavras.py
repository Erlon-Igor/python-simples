try:
    tipo = input('\nContar palavras de um arquivo ou de uma frase digitada por você? (a/f) ').strip().lower()
    
    if tipo not in 'a f':
        print('Digite "a" para arquivo ou "f" para frase do usuário!')
        print('Reinicie o programa e tente novamente.\n')

    elif tipo == 'a':
        lista_linhas = []
        lista_palavras = []
        nome_arquivo = input('Nome do arquivo (ex: arquivo.txt): ').strip()
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo.readlines():
                lista_linhas.append(linha.split(" "))
        
        for linha in lista_linhas:
            for palavra in linha:
                lista_palavras.append(palavra)
        print(f'Oh legal! o seu arquivo tem {len(lista_palavras)} palavras.\n')
        
    elif tipo == 'f':
        frase_usuario = input('O que você tem em mente hoje?\n').strip()
        print(f'Oh legal! você acabou de me dizer o que está pensando em {len(frase_usuario.split(" "))} palavras.\n')
except Exception as erro:
    print(f'\nAlgo de errado aconteceu!\nErro: {erro}\n')
