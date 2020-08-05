"""
POO - Polimorfismo
Poli->Muitas
Morfis->Formas
"""
class Animal:
    def __init__(self,nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')
    def comer(self):
        print(f'{self.__nome} está comendo...')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def falar(self):
        print(f'{self._Animal__nome} fala "miau"')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

miau1 = Gato('Estrela')
miau1.falar()
miau1.comer()

dog1 = Cachorro('Stark')
dog1.comer()
dog1.falar()

