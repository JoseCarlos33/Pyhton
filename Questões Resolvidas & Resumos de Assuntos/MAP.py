"""
MAP
-> Com map, mapeamos valores para jogar na função
"""
import math

def area(raio):
    #Calculando area do circulo:
    return math.pi * (raio**2)

raios = [2,4,5,6,7,8,9]

#maneira convenional:
areas = [area(r) for r in raios]
print(areas,end='\n\n')

#Utilizando map
areas2 = map(area, raios)
print(list(areas2))

#Utilizando map com lambda:
print(list(map(lambda r: math.pi * r**2,raios)))
print()

#OBS.:map so aceita interagir com função que possui somente 1 parametro de entrada
