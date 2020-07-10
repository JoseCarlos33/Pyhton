"""
Tuplas(tuple):
-> Sao bastante parecidas com listas
-> Existem basicamente duas diferenças básicas:
    1) As tuplas sao representadas por parenteses ()
    2) As tuplas sao imutaveis: Isso significa que ao criar uma tupla ela nao muda.
       Toda operaçao em uma tupla gera uma nova tupla
"""
"""
#CUIDADO! A Tupla é representada por parenteses mas pode haver variaçoes:

tupla1 = (1,2,3,4,5)
print(tupla1)
print(type(tupla1))
print("")
tupla2 = 1,2,3,4,5
print(tupla2)
print(type(tupla2))
print("")
tupla3 = (4) #REPRESENTAÇAO ERRADA, o python interpreta como inteiro
print(tupla3)
print(type(tupla3))
print("")
tupla4 = (4,) #REPRESENTAÇAO CORRETAAAAA, VAI PORRA
print(tupla4)
print(type(tupla4))
"""

"""
#Podemos gerar uma tupla dinamicamente com o range
tupla = tuple(range(10))
print(tupla)
print(type(tupla))
"""

#Desenpacotamento de tupla:
"""
tupla = ('josé','carlos')
nome1,nome2 = tupla
print(nome1)
print(nome2)
"""

#Comandos que funcionam quando uma tupla só possui numeros inteiros ou reais
"""
tupla = (1,2,3,4,5,6.5)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
"""

#Concatenaçao de tuplas
"""
tupla1 = (1,2,3)
print(tupla1)

tupla2 = (4,5,6)
print(tupla2)

print(tupla1+tupla2)
print(tupla1)
print(tupla2)
"""
"""
#Contando elementos em uma tupla:

tupla = ('a','a','a','b','b','c','d','e','f','f')
print(tupla.count('a'))

escola = tuple('Geek Games')
print(escola)
"""
"""
#Como achar indice de algum elemento da tupla:
meses = ('Janeiro', 'Fevereiro', 'Março')
print(meses.index('Março'))
"""

"""
OBSERVAÇAO:

Tuplas deixam o código mais rapido (bom para inteligencia artificial
)
"""