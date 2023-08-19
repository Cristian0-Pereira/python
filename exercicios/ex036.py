nome = str(input('Qual seu nome? '))
print(f'Seja bem vindo ao Banco Pan, {nome}')
casa = float(input('Qual o Valor da casa? R$ '))
salario = float(input('Qual seu salário? R$ '))
tempo = int(input('Em quantos Anos você pretende pagar o empréstimo? '))
prestacoes = tempo * 12
parcelas = casa / prestacoes
minimo = salario * 30 / 100
print(f'Para pagar a casa de R$ {casa:.2f} reais em {tempo} anos a prestação será de R$ {parcelas:.2f} reais.')
if parcelas <= minimo:
    print(f'EMPRÉSTIMO CONCEDIDO em {prestacoes:.0f} Parcelas de R$ {parcelas:.2f} reais, Parabéns!')
else:
    print('EMPRÉSTIMO NEGADO!')
print('Banco Pan agradece sua visita!')
