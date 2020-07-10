linha1 = input()
linha2 = input()
xa,ya = linha1.split()
xb,yb = linha2.split()
x1 = float(xa)
x2 = float(xb)
y1 = float(ya)
y2 = float(yb)
r1 = (x2-x1)**2
r2 = (y2-y1)**2
r3 = r1+r2
r4 = r3**(1/2)
print('%1.4f'%r4)