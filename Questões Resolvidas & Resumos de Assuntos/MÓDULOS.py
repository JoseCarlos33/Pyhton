
"""
COMO TRABALHAR COM MODULOS
"""

#Importando modulo criado por mim

from funçao_ex import soma

print(soma(1,2))

#dando apelido para import

from random import random as rd

print(rd())

#multiplos imports de um mesmo modulo

from random import (
    random,
    randint,
    choice,
    shuffle
)

print(random())
print(randint(3, 10))
print(choice('Universidade'))