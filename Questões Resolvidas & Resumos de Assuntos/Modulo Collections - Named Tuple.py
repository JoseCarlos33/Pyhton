"""
NAMED TUPLE
->Facilita a organizaçao de tuplas
"""

#Importando

from collections import namedtuple

#Criando tuplas com o Nmed Tuple

#Forma 1:
cachorro = namedtuple('cachorro','nome raça idade')

#Forma 2:
cachorro = namedtuple('cachorro','nome, raça, idade')

#Forma 3:
cachorro = namedtuple('cachorro',['nome', 'raça', 'idade'])

#Usando:

ray = cachorro(nome='Scolovisk',idade=3,raça='Pastor Alemao')

print(ray)
print(ray.idade)#biblioteca facilitando acesso a item da tupla
print(ray.raça)
