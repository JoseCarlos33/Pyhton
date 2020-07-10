dois_num = input().split()
L1,C1 = dois_num
L = int(L1)
C = int(C1)

#Lendo matriz como string
matriz_string = [input().split() for n in range(0,L)]#lendo como string as colunas

#Transformando matriz string em matriz com inteiros:
matriz = [[int(matriz_string[n][i]) for i in range(0,C)] for n in range(0,L)]

#fazendo divisão
lista_dividida = [[matriz[n][i]/2 if i % 2 == 0 else matriz[n][i] for i in range(C)] for n in range(L)]

#imprimindo matriz
[[print(int(lista_dividida[n][i]),end=' ') for i in range(C)]and print() for n in range(L)]
