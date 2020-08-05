"""
POO - Classes
Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente

Imagine que você queria fazer um sistema para automatizar o controle de lâmpadas da sua casa.

Classes podem conter:
    -Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto. No caso da lampada, possivelmente iríamos querer saber se a lâmpada é
    110 ou 220 volts, se ela é branca, amarela ou de outra cor, qual é sua luminosidade e etc.

   -Métodos(funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu
   sistema. No caso da lâmpada, por exemplo, um comportamento comum é o de ligar e desligar.

Em Python, dividimos os atributos em 3 grupos:
    -Atributos de Instância
    -Atributos de Classe
    -Atributos Dinâmicos

#Atributos de instância: são atributos declarados dentro do método construtor

#OBS.: Método construtor é um método especial para a construção do objeto

Todo atributo em python é público a não ser que utilizemos duplo underscore( __ ) antes do nome do atributo,
ex.: self.__nome = nome
isso torna o atributo privado, ou seja, só pode ser acessado dentro da própria classe
"""

class Lampada:
    def __init__(self, voltagem,cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self,numero,limite,saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    #Atributos de classe:
    imposto = 1.05
    contador = 0
    def __init__(self, nome, valor,id=0):
        self.valor = valor * Produto.imposto
        self.nome = nome
        self.id = Produto.contador + 1
        Produto.contador = self.id

a = Produto('celular',1000)
print(a.nome,a.id,a.valor)
b = Produto('bola de basquete',70)
print(b.nome,b.id,b.valor)