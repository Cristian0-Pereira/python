a = float(input('Digite um lado do Triângulo    -> '))
b = float(input('Digite outro lado do triângulo -> '))
c = float(input('Digite outro lado do Triângulo -> '))
if a < b + c and b < a + c and c < a + b:
    print('\33[34mVerdadeiro\33[m')
    if a == b == c:
        print('Triângulo EQUILÁTERO!')
    elif a != b != c != a:
        print('Triângulo ESCALENO!')
    else:
        print('Triângulo ISÓSCELES!')
else:
    print('\33[31mFalso\33[m')
