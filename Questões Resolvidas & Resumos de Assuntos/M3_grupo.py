dois_num = input().split()
L1, C1 = dois_num
L = int(L1)
C = int(C1)

#Lendo matriz como string:
matriz_string = [input().split() for n in range(0,L)]#lendo como string as colunas

#Transformando matriz string em matriz com inteiros:
matriz = [[int(matriz_string[n][i]) for i in range(0,C)] for n in range(0,L)]

#criando lista com soma das linhas:
soma_linhas = [sum(elementos) for elementos in matriz] #criando lista com soma das linhas
maior_linha = max(soma_linhas)

#criando lista com soma das colunas:
colunas = [[matriz[i][n] for i in range(0,L)] for n in range(0,C)]
maior_coluna = max(colunas)
soma = sum(maior_coluna)

if soma>maior_linha:
    print(soma)
else:
    print(maior_linha)
