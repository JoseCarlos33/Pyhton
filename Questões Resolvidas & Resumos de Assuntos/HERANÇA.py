"""
POO - Herança
-> O conceito de herança é basicamente aproveitamento de código
"""
#Exemplo

class Pessoa:
    def __init__(self, nome, sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def NomeCompleto(self):
        return print(f'Nome:{self.__nome}{self.__sobrenome}')

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome,cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
