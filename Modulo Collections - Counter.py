"""
MODULO COLLECTIONS - COUNTER

->Transforma um iteravel em um dicionario onde os valores do iterável vira a chave
  e o valor da chave é a quantidade de apariçoes do elemento.
->Ou seja, ele conta a quantidade de vezes que os valores aparecem na iteraçao.

"""

#REALIZANDO O IMPORT:

from collections import Counter

#Podemos usar qualquer iterável
lista = [1,1,2,2]
print(Counter(lista))

print(sum(Counter(lista)))


nume