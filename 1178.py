lista = []
for n in range(100):
    lista.append(0.0000)
n = float(input())
lista[0] = n
for num in range(1, 100):
    lista[num] = lista[num-1]/2
for num in range(100):
    print('N[%i] = %1.4f'%(num, lista[num]))
