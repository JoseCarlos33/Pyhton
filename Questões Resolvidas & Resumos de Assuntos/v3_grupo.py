num = int(input())
lista = input().split(' ')
lista1 = []
aux = 0
for i in range(num):
    lista1.append(int(lista[i]))
num2 = input().split()
num3 = int(num2[0])
num4 = int(num2[1])
aux = lista1[num3]
lista1[num3] = lista1[num4]
lista1[num4] = aux
for i in range(num):
    print(lista1[i],end=' ')
