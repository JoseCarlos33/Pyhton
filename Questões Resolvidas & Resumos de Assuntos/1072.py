rep = int(input())
dentro = 0
fora = 0
for n in range(0, rep):
    num = int(input())
    if num>=10 and num<=20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print(f'{dentro} in')
print(f'{fora} out')

