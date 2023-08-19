from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    comp = randint(0,10)
    soma = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o Computador {comp}. Total de {soma}')
    print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar Novamente...')
print(f'GAME OVER! Você Venceu {v} vezes.')
