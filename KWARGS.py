"""
KWARGS

->É um parametro de funçao que recebe dicionário
-> Nao é parametro obrigatorio
-> É declarado da seguinte forma **kwargs
-> Nao possui limite de elementos

OBSERVAÇAO:
 -> OS PARAMETROS DE UMA FUNÇAO DEVEM OBEDECER A SEGUINTE ORDEM:
    -Parametros obrigatorios
    -*args
    -Parametros default(opcionais)
    -**kwargs
    exemplo:
            def dados_pessoais(nome,sobrenome,*args,faculdade='UFBA',**kwargs)
"""
"""
#Exemplo 1:
def cores_preferidas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor preferida de {pessoa} é {cor}')

cores_preferidas(jose='Verde',joao='azul')

"""
"""
#Exemplo mais complexo:

def comprimentos(**kwargs):
    if 'Linguagem' in kwargs and kwargs['Linguagem']=='Python':
        return (f'Bem vindo programador Python')
    elif 'Linguagem' in kwargs:
        return(f'Bem vindo programador')
    return ('Bem vindo')

print(comprimentos(Nome='José',Linguagem='Python'))
print(comprimentos(Linguagem='Java'))
print(comprimentos(Nome='Joao'))
"""

#Desempacotando dicionarios para jogar na kwargs:

def mostra_dicionario(**kwargs):
    for chave,valor in kwargs.items():
        print(f'{chave} = {valor}')

dic1 = dict(nome1='josé',nome2='joao',nome3='maria',nome4='vanessa')
dic2 = dict(sobrenome1='noronha',sobrenome2='oliveira',sobrenome3='bittencourte',sobrenome4='azevedo')
mostra_dicionario(**dic1,**dic2) #Usamos o duplo asterisco(**) para desempacotar dicionarios



