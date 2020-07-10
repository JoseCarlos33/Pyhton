"""
All
->Retorna True se todos os elementos do iterável respeitarem as condições

Any
-> retorna True se qualquer um dos elementos do iterável respeitarem as condições
"""
#Exemplo de aplicação - all:

num = [i for i in range(100)]
print(num)
#imprime false caso o numero da lista iterada nao esteja contido na lista num
print(all([print(i) for i in [1,2,3,4,5,1000] if i in num]))

#Exemplo de aplicação - any:
#imprime false caso todos os numeros da lista iterada nao estejam contidos na lista num
print(any([i for i in [1001,2000,3,4000,5000,1000] if i in num]))