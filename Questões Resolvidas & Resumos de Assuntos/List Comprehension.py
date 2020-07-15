"""
LIST COMPREHENSION:

-> Cria lista a partir de iteravel de uma forma muito simples
->Sintaxe:
          [nome_do_iteravel for valor in nome_do_iteravel]
"""
"""
#Exemplos:
lista = [1,2,3,4,5]

print([itens+1 for itens in lista])

nomes = ['jose','carlos','noronha']

nome_completo = [nome.title() for nome in nomes]
print(nome_completo)
"""

#USANDO ESTRUTURAS CONDICIONAIS DENTRO DA LIST COMPREHENSION:

LISTA = [1,2,3,4,5,6]

pares = [numeros for numeros in LISTA if numeros%2 == 0]
impares = [numeros for numeros in LISTA if numeros%2 != 0]

print(pares)
print(impares)
