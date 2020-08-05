"""
Para trabalhar com data e hora o python
possui um built-in chamado datetime
"""
import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

#retorna data e hora corrente
print(datetime.datetime.now())

#replace para fazer ajustes de data e hora

inicio = datetime.datetime.now()
print(inicio)
inicio = inicio.replace(year=2023,hour=16,minute=0,second=0,microsecond=0)
print(inicio)

#criando um momento especifico com data e hora
evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))
print(type('31/08/2019'))

print(evento)

nascimento = input("Digite sua data de nascimento separando dia, mês e ano por '/' :  ")
nascimento = nascimento.split('/')

print(nascimento)
nascimento = datetime.datetime(int(nascimento[2]),int(nascimento[1]),int(nascimento[0]))
print(nascimento)
print(type(nascimento))

print(nascimento.year)#ano
print(nascimento.month)#mes
print(nascimento.day)#dia
print(nascimento.hour)#hora
print(nascimento.minute)#minuto
print(nascimento.second)#segundo
print(nascimento.microsecond)#microsegundos
dias_da_semana = ['Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo']
print(f'O dia da semana do nascimento foi: {dias_da_semana[nascimento.weekday()]}')# dia 0 = segunda-feira

#colocando a data no formato Brasileiro

formato_BR = nascimento.strftime('%d/%m/%Y')
print(formato_BR)