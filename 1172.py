valores = []
for n in range(10):
    valores.append(float(input()))
for i in range(10):
    if valores[i]<=0:
        valores[i] = 1
for num in range(10):
    print('X[%i] = %i'%(num, valores[num]))
