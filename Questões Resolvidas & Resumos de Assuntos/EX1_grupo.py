num1 = int(input())
num2 = input()
num3 = num2.split(' ')
converter_int = []
for i in range(num1):
    converter_int.append(int(num3[i]))
num4 = int(input())
if num4 in converter_int:
    print(num4)
else:
    print(-1)

