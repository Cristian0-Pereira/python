from datetime import date
ano = int(input('Digite o Ano OU Digite 0 para ano atual -> '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\33[33;1;7m{ano}\33[m é \33[34;1;4mBissexto!\33[m')
else:
    print(f'\33[31;1;7m{ano}\33[m \33[31;1mNão\33[m é \33[34;1;4mBissexto!\33[m')
