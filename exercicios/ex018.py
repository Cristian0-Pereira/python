from math import sin, cos, tan, radians
ang = int(input('Qual o ângulo?-> '))
seno = sin(radians(ang))
print(f'O ângulo de {ang}° tem o SENO de {seno:.2f}')
cosseno = cos(radians(ang))
print(f'O ângulo de {ang}° tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ang))
print(f'O ângulo de {ang}° tem a TANGENTE de {tangente:.2f}')
