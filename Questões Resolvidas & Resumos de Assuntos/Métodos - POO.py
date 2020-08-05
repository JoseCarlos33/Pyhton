"""
Métodos(funções) -> Representam os comportamentos que o objeto pode fazer em seu sistema
"""

class Produto:
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.id = Produto.contador + 1
        Produto.contador = self.id

    #método de instancia
    def desconto(self, desconto):
        d = 1-desconto/100
        return (self.valor * d)

produto1 = Produto("celular","android",1000)

print(produto1.desconto(10))
