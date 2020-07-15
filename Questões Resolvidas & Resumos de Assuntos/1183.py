matriz = [[],[],[],[],[],[],[],[],[],[],[]]


operacao = str(input())
soma = 0
for i in range(12):
    for n in range(12):
        val = float(input())
        matriz[i].append(val)
        if (n > i):
            soma += val
if operacao == 'S':
    print("%1.1f"%soma)
elif operacao == 'M':
    div = soma/12
    print("%1.1f"%div)
