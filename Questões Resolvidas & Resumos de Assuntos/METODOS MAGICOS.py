
class Filmes:
    def __init__(self,titulo,ano):
        self.__titulo = titulo
        self.__ano = ano

    def __str__(self):
        return f'{self.__titulo}'
    def __del__(self):
        return f'Os filmes foram deletados da memória'
filme1 = Filmes('velozes e furiosos',2005)
print(filme1)