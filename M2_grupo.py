N = int(input())
dois_num = input().split()
L1, C1 = dois_num
L = int(L1)
C = int(C1)

#Criando matriz NxN
matriz = [] #inicializando
[matriz.append([]) for n in range(0,N)] #criando linhas e colunas

#Lendo matriz como string:
matriz_string = []
[matriz_string.append(input().split()) for n in range(0,N)]#lendo como string

#Transformando matriz string em matriz com inteiros:
[[matriz[n].insert(i,int(matriz_string[n][i])) for i in range(0,N)] for n in range(0,N)]

#Contando valores
cont = 0
a=[]
[[a.append(matriz[n][i]) for i in range(0,N) if i==C-1 or n==L-1]for n in range(0,N)]

print(sum(a)-matriz[L-1][C-1])



