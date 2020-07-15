#linha1 = input()
#linha2 = input()
#xa,ya = linha1.split()
#xb,yb = linha2.split()
#x1 = float(xa)
#x2 = float(xb)
#y1 = float(ya)
#y2 = float(yb)
#r1 = (x2-x1)**2
#r2 = (y2-y1)**2
#r3 = r1+r2
#r4 = r3**(1/2)
#print('%1.4f'%r4)
valor = int(input())
if valor<1000000:
 cem = int(valor/100)
 cinq = int(valor%100/50)
 vinte = int(valor%100%50/20)
 dez = int(valor%100%50%20/10)
 cinco = int(valor%100%50%20%10/5)
 dois = int(valor%100%50%20%10%5/2)
 um = int(valor%100%50%20%10%5%2)

 print(valor)
 print('%i nota(s) de R$ 100,00'%cem)
 print('%i nota(s) de R$ 50,00'%cinq)
 print('%i nota(s) de R$ 20,00'%vinte)
 print('%i nota(s) de R$ 10,00'%dez)
 print('%i nota(s) de R$ 5,00'%cinco)
 print('%i nota(s) de R$ 2,00'%dois)
 print('%i nota(s) de R$ 1,00'%um)

