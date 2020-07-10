

val = int(input())
valores = [val,0,0,0,0,0,0,0,0,0,0]
for n in range(1,11):
    valores[n] = valores[n-1]*2
for num in range(11):
    print('N[%i] = %i'%(num, valores[num]))

