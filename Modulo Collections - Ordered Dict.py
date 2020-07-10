"""
Ordered Dict

-> Garante que o dicionario ira ser impresso na ordem correta em uma iteraçao
"""

from collections import OrderedDict

dicionario = OrderedDict({'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6})

for chave, valor in dicionario.items():
    print(f'{chave} = {valor}')
    print()
