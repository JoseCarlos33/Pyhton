"""
Listas:

-Sao dinamicas: podemos simplesmente criar uma lista e ir adicionando elementos nela
-Aceitam todos os tipos de dados
- Sao representadas entre colchetes

"""
"""
print(type([]))
lista1 = [1,33,3,4,5]
print(lista1)
lista2 = ['g','f','h','z']
print(lista2)
lista3 = []
print(lista3)
lista4 = list(range(11))
print(lista4)
lista5 = list('Geek University')
print(lista5)
print("")
"""
"""
#Ver se um certo elemento existe na lista
if 5 in lista1:
    print('O numero 5 está na lista')
else:
    print('O numero 5 nao está na lista')
print("")
"""
"""
#Podemos facilmente ordenar uma lista:
lista1.sort()
print(lista1)
print("")

#Podemos facilmente contar o numero de ocorrencias de um elemento numa lista:
print(lista5.count('e'))
print("")
"""
"""
#Podemos adicionar elementos numa lista:

#Usando append(1 elemento por vez):
print(lista1)
lista1.append(11)
print(lista1)
print("")

#Usando extend(mais de um elemento, ou elementos iteraveis,por exemplo, strings ou listas):
print(lista1)
lista1.extend([22,333,432])#OBS.: Para adicionar mais de um valor, coloque em forma de lista
print(lista1)
print("")
"""
"""
# Usando insert, para adicionar em algum indice especifico:
print(lista1)
lista1.insert(2, 223)# estrutura do insert -> lista.insert(indice, elemento para adicionar)
print(lista1)
print("")
"""
"""
#Para inverter uma lista usa-se a funçao reverse:
print(lista1)
lista1.reverse()
print(lista1)
print("")
"""
"""
#Para ver o tamanho de uma lista usar funçao len:
print(len(lista4))
print("")
"""
"""
#Remover elemento da lista, funçao pop:
#Removendo o ultio elemento:
print(lista4)
lista4.pop()
print(lista4)
print("")

#Removendo elemento pelo indice:
print(lista4)
lista4.pop(2)#o "2" é o indice em que haverá a remoçao do elemento
print(lista4)
print("")
# OBS.: os elementos a direita do indice sao deslocados para esquerda

#Para limpar toda a lista, funçao clear:
print(lista4)
lista4.clear()
print(lista4)
print("")
"""
"""
#Podemos repedir elementos em uma lista:
lista6 = [1,2,3]
lista6 = lista6 * 3
print(lista6)
print("")
"""
"""
#Para converter string em lista:

curso = 'Geek University: curso de python3'
print(curso)
curso = curso.split()
print(curso)
print("")
"""

"""
#Iterando em uma lista

#Com Loop For
lista_teste = [11,22,33]
for elemento in lista_teste:
    print(elemento)
print("")
#Com loop while
carrinho = []
produtos = ''

while produtos!='sair':
    print("Digite o nome do produto ou digite 'sair' para sair do carrinho:")
    produtos = input()
    if produtos!='sair':
        carrinho.append(produtos)
for produtos in carrinho:
    print(produtos)
print("")
"""

"""
#PARA GERAR INDICE:
cores = ['verde','azul','amarelo','rosa','vermelho']

for indice ,cor in enumerate(cores):
    print(indice,cor)
print("")
#Para ver indice de elemento especifico em uma lista:
print(cores.index('azul'))
print("")
"""
"""
#Slicing:

#lista[inicio:fim:passo]
#          ou
#rage(inicio:fim:passo)

numeros1 = [1,2,3,4,5]

print(numeros1[::])#Inicia no indice 0 e imprime até o final
"""
"""
#FORMAS DE COPIAR UMA LISTA:

#Forma 1:
lista1 = [1,2,3,4,5]
lista2 = lista1.copy()#Cria lista independente, ou seja, caso se altere a lista 1 a lista 2 nao sera modificada
lista1.append(11)
print(lista1)
print(lista2)
print("")

#Forma 2:
lista = [1,2,3,4,5]

lista_copia = lista #cria lista dependente, ou seja, se a lista se modifica, a lista copia tbm se modifica

lista.append(11)
print(lista)
print(lista_copia)
print("")
"""

lista = [[1,2,3,4,5],[2,4,6,8,10]]
L=2
C=5
lista_dividida = [[lista[n][i]/2 if i % 2 == 0 else lista[n][i] for i in range(C)] for n in range(L)]

print(lista_dividida)
