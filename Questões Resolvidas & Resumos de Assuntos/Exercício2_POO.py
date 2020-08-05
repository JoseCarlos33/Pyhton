class Agenda:
    pessoas = 0
    memoria = ({'nome':'','idade':'','altura':''},{'nome':'','idade':'','altura':''},
               {'nome':'','idade':'','altura':''},{'nome':'','idade':'','altura':''},
               {'nome':'','idade':'','altura':''},{'nome':'','idade':'','altura':''},
               {'nome':'','idade':'','altura':''},{'nome':'','idade':'','altura':''},
               {'nome':'','idade':'','altura':''},{'nome':'','idade':'','altura':''})
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.id = Agenda.pessoas + 1
        Agenda.pessoas = self.id
        Agenda.memoria[Agenda.pessoas-1]['nome']=self.nome
        Agenda.memoria[Agenda.pessoas-1]['idade'] =self.idade
        Agenda.memoria[Agenda.pessoas-1]['altura'] =self.altura

    def RemoverPessoa(self, nome):
        del nome

    @classmethod
    def BuscaPessoa(self,nome): #informa em qual posição da agenda está a pessoa
        [print(f'Posição: {i+1}',end='\n\n') for i in range(10) if Agenda.memoria[i]['nome'] == nome]

    @classmethod
    def All(self): #imprime os dados de todas as pessoas da Agenda
        for i in range(10):
            if Agenda.memoria[i]['nome'] != '':
                print('---------------')
                print(f'USUÁRIO {i+1}:')
                print(f'NOME = {Agenda.memoria[i]["nome"]}')
                print(f'IDADE = {Agenda.memoria[i]["idade"]}')
                print(f'ALTURA = {Agenda.memoria[i]["altura"]}')
                print('---------------',end='\n\n')

    @classmethod
    def ImprimePessoa(self, id): #imprime o dados da pessoa na posição id da Agenda
        print('---------------')
        print(f'USUÁRIO {id}:')
        print(f'NOME = {Agenda.memoria[id-1]["nome"]}')
        print(f'IDADE = {Agenda.memoria[id-1]["idade"]}')
        print(f'ALTURA = {Agenda.memoria[id-1]["altura"]}')
        print('---------------', end='\n\n')


p1 = Agenda("josé",21,1.78)
p2 = Agenda("joao",20,1.77)

Agenda.BuscaPessoa('joao')
Agenda.All()
Agenda.ImprimePessoa(2)


