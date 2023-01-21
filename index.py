import random

while True:
    print('''
            Salve, salve caro usuário, hoje iremos gerar uma quantidade de senhas escolhidas pelo usuário com a quantidade de caracteres também escolhida pelo usuário.      
    ''')
    possivel = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!',.;:/\|@#$%¨&*()_-=+{[}]~^º°ª"
    quantidadeSENHAS = int(input('Digite a quantidade de senhas: '))
    quantidadeCARACTERES = int(input('Digite a quantidade de caracteres: '))
    tam = len(possivel)
    for i in range(quantidadeSENHAS):
        senha = str()
        for i in range(quantidadeCARACTERES):
            senha += random.choice(possivel)
        print(senha)
    if int(input('Deseja continuar? 0 para SIM e 1 para NÃO: ')) == 1: break