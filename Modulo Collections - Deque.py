"""
DEQUE
->Cria uma lista com funcionalidades novas de interaçao tanto com o inicio quanto com o final da lista
"""

from collections import deque

lista_string = deque('geek')
lista = list('geek')

print(lista_string)
print()
print(lista)

#FUNCIONALIDADES NOVAS

lista_string.appendleft('KKK')#insere no inicio
print(lista_string)
a = lista_string.popleft()#remove no começo e coloca em 'a' o valor removido
print(a)
print(lista_string)
