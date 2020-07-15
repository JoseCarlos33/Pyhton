"""
LAMBDAS:
->São funções sem nome, ou seja, anônimas
->sao criadas com somante uma linha
"""
#exemplo de simples

op = lambda x: x*2 + 1 #Estrutura: lambda parâmetro: operação que irá ser retornada da função

print(op(2))

#mais exemplos

autores = ['Monteiro Lobato','José de Alencar','Cecília Meireles','Carlos Drummond de Andrade ']

autores.sort(key=lambda nome:nome.split(' ')[-1].lower())#função sort ordena lista

print(autores)

def funcao_quadratica(a,b,c):
    return lambda x: a*x**2 + b*x + c

calculo = funcao_quadratica(5,3,4)#passa parametro a,b e c
print(calculo(2))#passa parametro x
