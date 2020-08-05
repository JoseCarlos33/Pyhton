class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def Imprimir(self):
        print(self.__nome)
        print(self.__endereco)
        print(self.__telefone)

class Cliente(Pessoa):
    def __init__(self,nome, endereco, telefone):
        super().__init__(nome, endereco, telefone)

p1 = Cliente('José', 'Rua do...', 5571)
p1.Imprimir()