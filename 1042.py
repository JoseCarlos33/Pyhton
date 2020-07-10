linha = input()
a,b,c = linha.split()
x1 = int(a);x2 = int(b);x3 = int(c)
lista_original = [x1,x2,x3]
lista_ordenada = [x1,x2,x3]
aux=0
for n in range(3):
    for i in range(3):
        if lista_ordenada[n]<lista_ordenada[i]:
            aux = lista_ordenada[n]
            lista_ordenada[n] = lista_ordenada[i]
            lista_ordenada[i] = aux
            print(f'n é : {n}; i é : {i}; lista ordenada[{n}] = {lista_ordenada[n]}')

for n in range(3):
    print(lista_ordenada[n])
    if n==2:
        print("")
for n in range(3):
    print(lista_original[n])
