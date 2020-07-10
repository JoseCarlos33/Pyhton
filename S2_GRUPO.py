alfabeto = ['a','b','c','d','e','f','g','h','i']

numeros = []
numeros_convertidos = []
codigo = input()
numeros = list(codigo)

for num in numeros:
    numeros_convertidos.append(int(num))

for valor in numeros_convertidos:
    print(alfabeto[valor-1],end='')

