print('-=-' * 15)
print('        Vamos Formar um Triângulo?')
print('-=-' * 15)
a = float(input('Digite um lado do Triângulo    -> cm '))
b = float(input('Digite outro lado do triângulo -> cm '))
c = float(input('Digite outro lado do Triângulo -> cm '))
if a < b + c and b < a + c and c < a + b:
    print('\33[34mVerdadeiro\33[m')
else:
    print('\33[31mFalso\33[m')
