from time import sleep
print(f'{"LOJAS PIUDIPIUBR":=^40}')
valor = float(input('Qual o valor Total da compra? R$ '))
num = int(input('''=-=-=FORMAS DE PAGAMENTO=-=-=
1- À Vista no Dinheiro ou Cheque (10% Desconto)
2- À Vista no Cartão (5% Desconto)
3- Em 2x no Cartão (Sem Juros)
4- Em 3x ou mais no Cartão (20% de Juros)
===Digite a opção=== -> '''))
sleep(1.5)
final = 0
if num == 1:
    x1 = valor - (valor * 10 / 100)
    print(f'Á vista com 10% de desconto -> R$ {x1:.2f} reais <-')
    final = 1
elif num == 2:
    x2 = valor - (valor * 5 / 100)
    print(f'À vista no cartão com 5% de desconto -> R$ {x2:.2f} reais <-')
    final = 1
elif num == 3:
    x3 = valor / 2
    print(f'Você pagará em 2x sem Juros de -> 2x de R$ {x3:.2f} reais no Cartão <-')
    final = 1
elif num == 4:
    x4 = valor + (valor * 20 / 100)
    parcelas = int(input('Quantas parcelas: '))
    print(f'''Você parcelou R$ {valor:.2f} reais em {parcelas}x com juros de 20% no cartão
e sairá por R$ {x4:.2f} reias em {parcelas}x de R$ {x4 / parcelas:.2f} reais.''')
    final = 1
else:
    print(f'{"Opção Inválida":=^40}')
if final == 1:
    print(f'{"Obrigado e Volte sempre":=^40}')
