velo = int(input('Qual Velocidade do Carro em km/h -> '))
print('Velocidade máxima permitida de 80 km/h')
print(f'Sua velocidade é de >>> {velo} km/h <<<')
if velo <= 80:
    print('          Parabéns!')
else:
    print('Você excedeu o Limite de velocidade!')
    print(f'Você será multado em R$ {(velo - 80) * 7:.2f} reais\n           Obrigado!')
