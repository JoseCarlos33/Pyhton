idade = int(input())
anos = idade/365
meses = idade%365/30
dias = idade%365%30

print('%i ano(s)'%anos)
print('%i mes(es)'%meses)
print('%i dia(s)'%dias)

