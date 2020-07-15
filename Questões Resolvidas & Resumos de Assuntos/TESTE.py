dicionario1 = {'a':1,'b':2,'c':3,'d':4}

novo_dict = {chave:valor+1 for chave,valor in dicionario1.items()}
print(novo_dict)

#transformando string e lista em dicionario:

string1 = 'abcde'
lista1 = [1,2,3,4]

print({string1[i]:lista1[i] for i in range(4)})
