from random import randint
from time import sleep
comp = randint(0, 5)  # Computador sorteia um número
usuario = int(input('Digite um número de 0 - 5 -> '))  # Usuário tenta acertar
print('........PROCESSANDO.......')
sleep(3)
print('        Computador', comp)
print('        Você  --- ', usuario)
print('-=-' * 10)
if comp == usuario:
    print('        Você Acertou!')
else:
    print('        Você Errou!')
