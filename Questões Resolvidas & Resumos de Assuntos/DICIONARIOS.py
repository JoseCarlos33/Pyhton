"""
DICIONARIOS:
-> Sao representaçoes do tipo chave e valor;
->Ex.:
      -> nas listas as chaves sao os indices e os valores é o que está contido nos indices
-> no dicionario fica explicito a chave e o valor associado a ela e nao  implicito como no caso das listas
-> Dicionarios sao representados por chaves {}
"""

"""
#CRIANDO DICIONARIOS:

#Forma 1:

paises = {'br':'Brasil', 'us':'Estados Unidos'}

print(paises)
print(type(paises))
print("")
#Forma 2:

paises2 = dict(br='brasil',us='Estados Unidos')
print(paises2)
print(type(paises2))
print("")
"""
"""
#ACESSANDO OS ELEMENTOS DO DICIONARIO:

#FORMA 1(menos recomendada):

paises = {'br':'Brasil', 'eua':'Estados Unidos','ru':'Russia'}

print(paises['ru'])
print()

#FORMA 2 (RECOMENDADA):

paises = {'br':'Brasil', 'eua':'Estados Unidos','ru':'Russia'}

print(paises.get('br'))
print()
#Obs.: Utilizando o 'get' evita-se erro na compilaçao caso nao ache o elemento

pais = paises.get('br')
if pais:
    print(f'Pais está catalogado como "{pais}"')
else:
    print('Pais nao catalogado')
"""
"""
#Os dicionarios podem conter dados de TIPOS DIFERENTES:

cardapio = {'camarao': 100, 'espaguete':50}
pedido = cardapio.get('camarao')
if pedido:
    print('Vou querer um por favor')
else:
    print("Escolheremos outro prato")
"""
"""
#Como adicionar itens em um dicionario:

#Forma 1:

Produtos = {'calça':110, 'blusa':20, 'tenis':100}
print(Produtos)
Produtos['anel']=30
print(Produtos)
print()

#Forma 2:

novo_produto = {'aliança':200 }
Produtos.update(novo_produto)
print(Produtos)
print()
"""
"""
#Remover itens de um dicionario:

#Forma 1:

faturas = {'jan':100, 'fev':100, 'mar':100}
print(faturas)
faturas.pop('jan')
print(faturas)
print()

#Forma 2:

del faturas['mar']
print(faturas)
print()
"""
"""
#Copiar Dicionário:

#Forma 1:

receita = {'farinha': 2, 'leite': 1}

receita_copia1 = receita.copy()
receita_copia1['banana'] = 5
print(receita)
print(receita_copia1)
print()

#Forma 2:

receita_copia2 = receita
receita_copia2['chocolate'] = 1
print(receita)
print(receita_copia2)
print()
"""
