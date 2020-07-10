num = int(input())
impares = 1
resto = num%2
if resto==0:
    while impares<num:
        print(impares)
        impares = impares + 2
else:
    while impares<=num:
        print(impares)
        impares = impares + 2

