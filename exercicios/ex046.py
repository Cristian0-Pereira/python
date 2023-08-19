"""Contagem Regressiva"""
from time import sleep
for c in range(10 , -1, -1):
    print(f'{c:=^22}')
    sleep(1)
print(f'{"FELIZ ANO NOVO":☺^20}')
