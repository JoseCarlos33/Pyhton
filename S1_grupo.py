senha = []
for i in range(6):
    palavra = input()
    tam = len(palavra)
    senha.append(tam)

for i in range(6):
    print(senha[i],end='')
    