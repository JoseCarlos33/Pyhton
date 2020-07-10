"""
FUNÇOES:

-> No Python funçoes sao definidas por def
-> Ex.: def diz_oi():
            print('Oi!')

"""
"""
#Funçoes com retorno

def quadrado_de_7():
    return 7 * 7

a = quadrado_de_7()
print(a)
print()

from random import random

def joga_moedas():
    if random() > 0.5:
        return 'Cara'#OBS.: O return finaliza o codigo quanto ativado
    return 'Coroa'

print(joga_moedas())

#FUNÇOES COM RETORNO

#EXEMPLO:

def quadrado(numero):
    return numero ** 2

usuario = int(input('Digite o número: '))
q = quadrado(usuario)
print(f'O numero {usuario} ao quadrado é igual a {q}')
print()

#FUNÇOES COM PARAMETROS OBRIGATORIOS:

def soma_impares(lista):
    total = 0
    for impar in lista:
        if impar % 2 !=0:
            total += impar
    return total

numeros = []
for i in range(5):
    if i == 4:
        print('Atençao, ultimo numero da lista!')
    numeros.append(int(input(f'Inserir número na posiçao {i}: ')))

print(soma_impares(numeros))
"""
"""
#FUNCOES COM PARAMETRO OPCIONAL:

def exponencial(numero, potencia = 2):#Caso nao seja dita a potencia pelo usuario, por padrao usara 2(quadrado)
    return numero ** potencia
a = input('Digite o numero e a potencia que deseja elevar a esse numero: ')
a1,a2 = a.split()
b1 = int(a1)
b2 = int(a2)
print(exponencial(b1, b2))
"""

"""
#Passando uma funçao como parametro:

def soma(num1=0, num2=0):
    return num1+num2
def subtracao(num1=0, num2=0):
    return num1-num2
def equacao(num1=0, num2=0, func=soma):
    return func(num1,num2)

numer1 = int(input('Digite o primeiro número da operaçao: '))
numer2 = int(input('Digite o segundo número da operaçao: '))
operac = int(input('Digite 1 para somar e 2 para subtrair: '))
a = 0
if operac == 1:
    a = equacao(numer1, numer2, soma)
elif operac == 2:
    a = equacao(numer1, numer2, subtracao)
print(f'O resultado da operaçao foi {a}')
"""
"""
#Usando variavel global:

palavra = 'jose'

def imprima_nome():
    global palavra
    palavra = palavra + 'carlos'
    print(palavra)

entrada = input()
if entrada == 'a':
    a = imprima_nome()
"""
