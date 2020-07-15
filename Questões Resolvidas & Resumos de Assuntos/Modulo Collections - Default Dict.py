"""
Modulo Collections - Default Dict

#Recapitulaçao Dicionários

dicionario = {'curso': 'Programaçao em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) #GERA KEYERROR

Default Dict -> Ao criar um dicionario utilizando Default Dict, nós informamos um valor default
podendo utilizar um lambda para isso. Este valor será utilizado sempre que nao houver um valor definido.
Caso tentemos acessar uma chave que nao existe, essa chave será criada e o valor default será atribuido.
"""

#Fazendo importaçao

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)
print(dicionario['outro'])#KeyError sem o modulo, mas aqui nao
print(dicionario)


