from time import sleep
import emoji
from random import randint
itens = ['','Pedra', 'Papel', 'Tesoura']
computador = randint(1, 3)
itens[1] = (emoji.emojize(':fist:', use_aliases=True))
itens[2] = (emoji.emojize(':raised_hand_with_fingers_splayed:', use_aliases=True))
itens[3] = (emoji.emojize(':v:', use_aliases=True))
print('''=-=-=Vamos jogar Jokenpô?=-=-=
=-=-=Suas opções=-=-=
[1] \33[33;1mPedra\33[m
[2] \33[31;1mPapel\33[m
[3] \33[32;1mTesura\33[m''')
jogador = int(input('Qual sua jogada? '))
if jogador != 1 and jogador != 2 and jogador != 3:
    print(f'{"JOGADA INVÁLIDA":^30}')
else:
    print(f'{"JO":=^30}')
    sleep(0.5)
    print(f'{"KEN":=^30}')
    sleep(0.5)
    print(f'{"PÔ":=^30}')
    sleep(0.5)
    print('-=' * 14)
    sleep(0.5)
    print('Jogador', itens[jogador], 'x', itens[computador], 'Computador')
    if computador == 1:  # computador jogou PEDRA
        if jogador == 1:
            print(f'{"EMPATE":^30}')
        elif jogador == 2:
            print('\33[34;1m       JOGADOR VENCEU\33[m')
        elif jogador == 3:
            print('\33[34;1m       COMPUTADOR VENCEU\33[m')
    elif computador == 2:  # computador jogou PAPEL
        if jogador == 1:
            print('\33[34;1m      COMPUTADOR VENCEU\33')
        elif jogador == 2:
            print(f'{"EMPATE":^30}')
        elif jogador == 3:
            print('\33[34;1m       JOGADOR VENCEU\33[m')
    elif computador == 3:  # computador jogou TESOURA
        if jogador == 1:
            print('\33[34;1m        JOGADOR VENCEU\33[m')
        elif jogador == 2:
            print('\33[34;1m      COMPUTADOR VENCEU\33[m')
        elif jogador == 3:
            print(f'{"EMPATE":^30}')
    print('Vamos Brincar de novo', emoji.emojize(':jack_o_lantern:', use_aliases=True))
