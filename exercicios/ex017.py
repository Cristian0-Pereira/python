from math import hypot
cOpo = float(input('Digite o Cateto Oposto :-> '))
cAdj = float(input('Digite o Cateto Adjacente :-> '))
# hip = sqrt(pow(cOpo, 2) + pow(cAdj, 2))
# print(f'A Hipotenusa é {hip:.1f}')
hip = hypot(cOpo, cAdj)
print(f'A hipotenusa vai medir {hip:.1f}')
