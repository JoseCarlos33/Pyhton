"""
SORTED

-> Sorted() é DIFERENTE de sort(), pois sort() funciona somente com listas.
->sorted() organiza QUALQUER iterável
-> Sorted() cria uma cópia ordenada do iterável, não alterando o iterável
   original.
"""
lista = [55,22,33,44,11]
tupla = 55, 22, 33, 44, 11,
dicionário = {'d': 4,'a': 1, 'c': 3, 'b':2}
conjunto = {4,3,1,2}

#Ordenando do MENOR para o MAIOR:
print(sorted(lista))
print(sorted(tupla))
print(sorted(dicionário))
print(sorted(conjunto))
print()

#Ordenando do MAIOR para o MENOR:
print(sorted(lista, reverse=True))
print(sorted(tupla, reverse=True))
print(sorted(dicionário, reverse=True))
print(sorted(conjunto, reverse=True))

#Exemplo mais complexo:
usuarios_twitter = [
    {'username': 'José' ,'tweets': []},
    {'username': 'João' ,'tweets': ['adoro bolos','comer é vida']},
    {'username': 'Geovana' ,'tweets': []},
    {'username': 'Bruna' ,'tweets': []},
    {'username': 'Camila' ,'tweets': []},
    {'username': 'Matheus' ,'tweets': []}
]
#Ordenando por ordem alfabética
print(sorted(usuarios_twitter, key=lambda usuarios: usuarios['username']))

#Ordenando pelo tamanho do nome(nome mais curto até nome mais cumprido)
print(sorted(usuarios_twitter, key=lambda usuarios: len(usuarios['username'])))
