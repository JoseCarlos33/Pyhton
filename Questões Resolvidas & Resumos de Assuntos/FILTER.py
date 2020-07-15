""""
FILTER
filter() -> serve para filtrar determinada coleção
"""
#Biblioteca para trabalhar com dados estatísticos
import statistics
dados = [1.0,3.8,2.8,4.3,-0.1]

#Calculando a média dos dados utilizando a função mean
media = statistics.mean(dados) #mean calcula a média

print(f'Média: {media}')

"""OBS.: assim como a função map(), a função filter recebe dois
parâmetros: uma função e um iterável."""

result = filter(lambda x: x > media, dados)
print(list(result))

print(f'{list(result)}')
#Assim como na função map, após utilizar os dados de filter
# ele desaparece da memória

paises = ['', 'Argentida', '', 'Brasil', '', 'Venezuela', '']

new_paises = filter(None, paises)
#filter apaga dados do tipo None
print(list(new_paises))

#Diferença entre map() e filter():

#Map() -> retorna um objeto mapeandi a função para cada elemento do iterável
#Filter() -> retorna um objeto filtrando apenas os elementos de acordo com a função.

#Exemplo mais complexo:

usuarios_twitter = [
    {'username': 'José' ,'tweets': []},
    {'username': 'João' ,'tweets': ['adoro bolos','comer é vida']},
    {'username': 'Geovana' ,'tweets': []},
    {'username': 'Bruna' ,'tweets': []},
    {'username': 'Camila' ,'tweets': []},
    {'username': 'Matheus' ,'tweets': []}
]

print(usuarios_twitter, end='\n\n')

#forma 1
inativos1 = list(filter(lambda usuarios: usuarios['tweets']==[], usuarios_twitter))
[print(i, end='\n\n') for i in inativos1]
print()
#forma 2
inativos2 = list(filter(lambda usuarios: not usuarios['tweets'], usuarios_twitter))
[print(i, end='\n\n') for i in inativos2]
