from datetime import date
salario = float(input('Qual o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    aumento = '15%'
else:
    novo = salario + (salario * 10 / 100)
    aumento = '10%'
print(f'''\33[33mAntigo Salário\33[m era de R$ \33[33;40m{salario:.2f}\33[m reais
Passa a ser de R$ \33[31;40m{novo:.2f}\33[m reais a partir de \33[4;35m{date.today()}\33[m
Com aumento de \33[34m{aumento}\33[m''')
