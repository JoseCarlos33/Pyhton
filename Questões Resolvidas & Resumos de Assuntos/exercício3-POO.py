
class Elevador:
    max_pessoas = 0
    max_andares = 0
    num_pessoas = 0
    num_andar = 0
    def __init__(self,capacidade,andares):
        self.capacidade = capacidade
        self.andares = andares
        Elevador.max_pessoas = self.capacidade
        Elevador.max_andares = self.andares
    @classmethod
    def Entra(self):#acrescenta 1 pessoa no elevador, mas só se houver espaço
        if Elevador.num_pessoas < Elevador.max_pessoas:
            Elevador.num_pessoas += 1
            return print(f'O elevador agora tem {Elevador.num_pessoas} pessoa(s)')
        return print('Elevador cheio, aguarde um estante')

    @classmethod
    def Sai(self):#remove uma pessoa do elevador, mas somente se houver alguém dentro
        if Elevador.num_pessoas > 0:
            Elevador.num_pessoas -= 1
            return print(f'O elevador agora tem {Elevador.num_pessoas} pessoa(s)')
        return print('Elevador vazio')

    @classmethod
    def Sobe(self):#sobe 1 andar se já não estiver no último andar
        if Elevador.num_andar < Elevador.max_andares:
            Elevador.num_andar += 1
            return print(f'Subindo... Estamos agora no {Elevador.num_andar}º andar')
        return print('Elevador já se encontra no último andar')

    @classmethod
    def Desse(self):# desde 1 andar se já não estiver no terreo
        if Elevador.num_andar > 0:
            Elevador.num_andar -= 1
            return print(f'Descendo... Estamos agora no andar {Elevador.num_andar}')
        return print('Elevador já se encontra no último andar')

elevador = Elevador(5,15)

Elevador.Sobe()
Elevador.Desse()
[Elevador.Sobe() for i in range(3)]
Elevador.Entra()
[Elevador.Entra() for i in range(5)]