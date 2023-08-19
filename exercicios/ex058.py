from random import randint
jogador = cont = 0
comp = randint(0, 10)
print('''Sou seu Computador....
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
while jogador != comp:
    jogador = int(input('Qual seu palpite: '))
    cont += 1
    if jogador < comp:
        print('Mais... Tente mais uma vez')
    elif jogador > comp:
        print('Menos... Tente mais uma vez')
print(f'Acertou com {cont} tentativas. Parabéns!')
