dois_num = input().split()
L1, C1 = dois_num
L = int(L1)
C = int(C1)
#Criando matriz NxN
matriz = [] #inicializando
[matriz.append([]) for n in range(0,L)] #criando linhas

#Lendo matriz como string:
matriz_string = []
[matriz_string.append(input().split()) for n in range(0,C)]#lendo como string as colunas

#Transformando matriz string em matriz com inteiros:
[[matriz[n].insert(i,int(matriz_string[n][i])) for i in range(0,C)] for n in range(0,L)]

#criando lista com soma das linhas:
soma_linhas=[]
soma_linhas = [sum(elementos) for elementos in matriz] #criando lista com soma das linhas
[print(soma_linhas[i], end=' ') for i in range(L)]#imprimindo soma dos valores das linhas
print()
#criando lista com soma das colunas:
soma_colunas = []
colunas = []
[colunas.append([]) for n in range(0,C)]
[[colunas[i].insert(n,matriz[n][i]) for i in range(0,L)] for n in range(0,C)]
soma_colunas = [sum(colunas[n]) for n in range(C)]
[print(elementos, end=' ') for elementos in soma_colunas]

