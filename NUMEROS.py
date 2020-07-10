
#   TIPOS NUMERICOS
#   int -> numeros inteiros
#   float -> numeros reais
#   bool -> 0 ou 1
#   str -> string

#num1 = float(input())
#num2 = float(input())
#num3 = float(input())

#media = (num1* 2+num2*3+num3*5)/10
#print("MEDIA = %1.1f" % media)


linha = input()
a, b, c = map(float, linha.split())
delta = (b*b-4*a*c)
if delta<0:
    print('Impossível Calcular')
elif delta==0:
    r1 = (-b + ((b * b - 4 * a * c) ** (1 / 2))) / (2 * a)
    r2 = r1
    print('R1 = %1.5f' % r1)
    print('R2 = %1.5f' % r2)
else:
    r1 = (-b + ((b * b - 4 * a * c) ** (1 / 2))) / (2 * a)
    r2 = (-b - ((b * b - 4 * a * c) ** (1 / 2))) / (2 * a)
    print('R1 = %1.5f'%r1)
    print('R2 = %1.5f'%r2)

