
"""
for no python:

for item in iteravel:
 
range(1,10)
1
2
3
4
5
6
7
8
9
"""
qtd = int(input('Digite a quantidade de loops: '))
soma = 0
num = 0
for l in range(1, qtd+1):
    print(f'{l}')
print('')
for n in range(1, qtd+1):
    num = int(input(f'Digite o número {n} de {qtd}:'))
    soma = soma + num
print(f'A soma foi igual a {soma}')

"""
------------------------------------------------------
      COMO NAO PULAR LINHA DEPOIS DE UM PRINT:
------------------------------------------------------
"""

# print('nome', end='')

#Observaçao: para
