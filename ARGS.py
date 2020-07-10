"""
ARGS

->É um parametro de funçoes que permite passar mais informaçoes que o numero de parametro
  contido nas funçoes

->Os dados recebidos por args sao convertidos em uma tupla, entao operamos o args tal
  como operamos uma tupla

-> O parametro é escrito com asterisco(*) antes, ficando assim: *args

"""

#EXEMPLOS:

def soma_de_valores(*args):
    return sum(args)
inteiro = []
for i in range(3):
    inteiro.append(int(input(f'Insira o número {i+1}: ')))
print(inteiro)

print(soma_de_valores(*inteiro))#asterisco(*) antes da lista desempacota lista e passa somente os valores contidos na lista
print(soma_de_valores(1,2,3,4,5,6))