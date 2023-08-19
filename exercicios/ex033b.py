n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
lista = n1, n2, n3
ordenada = sorted(lista)
print(f'\33[33m{ordenada[0]}\33[m é o \33[34mmenor\33[m número!')
print(f'\33[31m{ordenada[-1]}\33[m é o \33[34mmaior\33[m número!')
