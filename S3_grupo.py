def contar_consoantes(string, T):
    cont = 0
    for n in range(len(string)):
        if string[n] in 'aeiou':
            cont += 0
        elif string[n]!=' ':
            cont += 1
    # print(f'Numero de consoantes é {cont}')#numero de consoantes
    if cont > T:
        return 0 #doar livro
    return 1 #ficar com livro

inteiros = input()
a1,a2 = inteiros.split()
N = int(a1)#quantidade de livros
T = int(a2)#quantidade consoantes

for i in range(N):
    nome_do_livro = input()
    print(contar_consoantes(nome_do_livro, T))


