FIB = [0,1,1]
for i in range(3,61):
    FIB.append(FIB[i-1]+FIB[i-2])

val = int(input())
for n in range(val):
    num = int(input())
    if(num<=60):
        print('Fib(%i) = %i'%(num,FIB[num]))