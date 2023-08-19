km = float(input('Qual a distância a percorrer? '))
preco = km * 0.5 if km <= 200 else km * 0.45
print(f'Você pagará \33[34;1;4;7mR$ {preco:.2f}\33[m  por \33[31;1;4m{km:.0f}\33[m quilômetros percorridos.')
print('                 \33[7;4;33mObrigado e Boa Viagem!\33[m')
