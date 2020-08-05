
def sendo_educado(funcao):
    def sendo():
        print('Oi,tudo bem?')
        print(funcao())
        print('Qual o seu nome?')
    return sendo

@sendo_educado
def Apresentando():
    return 'Me chamo José'

Apresentando()


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def pedindo_com_fome(principal, sobremesa):
    return f'O prato principal será {principal} e para a sobremesa vou querer {sobremesa}'

print(pedindo_com_fome('lasanha','rocanbole'))