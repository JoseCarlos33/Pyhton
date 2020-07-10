"""
CONJUNTOS:

-> Faz referencia aos conjuntos da matemática
-> No python sao conhecidos como sets.

-> Sets (conjuntos) nao possuem valores duplicados.
-> Sets (conjuntos) sao sempre ordenados.
-> Os sets sao referenciados por chaves {}

-> Diferença entre sets(conjuntos) e dicionários:
    ->Dicionarios tem chave e valor, os conjuntos só possuem valores;
"""
"""
#Definindo Conjuntos:

#Forma 1:
conjunto = {3, 4, 2, 1}
print(conjunto)
print(type(conjunto))
print()
#Forma 2:
set1 = set({1,2,2,2,5,4,3})
print(set1)
print(type(set1))
print()
"""
"""
#Uso interessante ddos conjuntos:
#Exemplo:

#Imagine a situaçao que alunos colocam em um cadastro no museu suas cidades de origem
#E um aplicativo gera uma lista com as cidades:

lista = ['Belo Horizonte','Sao Paulo', 'Bahia', 'Belo Horizonte', 'Bahia']

#Havendo cidades repetidas utilizamos os conjuntos para saber quantas cidades distintas possui a lista

cidades_distintas = set(lista) #transforma a lista em um conjunto(onde o conjunto tirara os valores repetidos##  # )

print(len(cidades_distintas))
"""
"""
#ADICIONANDO E REMOVENDO ELEMENTOS DE UM CONJUNTO:

#ADICIONANDO:
c = {1,2,3,4}
c.add(6)
c.add(6)
print(c)
print()

#REMOVENDO:

c.remove(4)
print(c)
print()
"""
"""
#UNINDO DOIS CONJUNTOS:

#Usando o Union:
estudante_python = {'Matheus','José','Cesar'}
estudante_javascript = {'José','Carlos'}

uniao = estudante_javascript.union(estudante_python)
print(uniao)
print()

#Usando |  :
uniao2 = estudante_python | estudante_javascript
print(uniao2)
print()
"""
"""
#Achando a intersecao dos conjuntos(elementos contidos em ambos):

estudante_python = {'Matheus','José','Cesar'}
estudante_javascript = {'José','Carlos'}

#Forma 1:
intersecao = estudante_javascript.intersection(estudante_python)
print(intersecao)
print()

#Forma 2:
intersecao2 = estudante_javascript & estudante_python
print(intersecao2)
print()
"""
"""
#Achando os valores contidos somente em um dos conjuntos:

estudante_python = {'Matheus','José','Cesar'}
estudante_javascript = {'José','Carlos'}

val1 = estudante_python.difference(estudante_javascript)#Estudantes que so estudam python
print(val1)
print()

val2 = estudante_javascript.difference(estudante_python)#Estudantes somente de javascript
print(val2)
print()
"""