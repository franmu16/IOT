#Esercizio 1
ci = int(input("Inserire capitale iniziale: "))
while (ci < 0):
    ci = int(input("Inserire capitale iniziale: "))
tia = int(input("Inserire tasso interesse annuo: "))
while (tia < 0):
    tia = int(input("Inserire tasso interesse annuo: "))
a = int(input("Inserire numero di anni: "))
while (a < 0):
    a = int(input("Inserire numero anni: "))

imp_finale = ci * (1 + tia/100)**a

print("Importo finale: " + str(imp_finale))

#Esercizio 2
num = int(input("Inserire numero intero positivo: "))
while (num < 0):
    num = int(input("Inserire numero intero positivo: "))

i = 0;
for val in str(num):
    i += 1

print("Numero cifre: " + str(i))

#Esercizio 3
num = int(input("Inserire numero intero positivo: "))
while (num < 0):
    num = int(input("Inserire numero intero positivo: "))
f
for i in range(num,1,-1):
    f = f*i;
    
print("Fattoriale : " + str(f))

#Esercizio4
import math

a = int(input("Inserire coefficienti a: "))
b = int(input("Inserire coefficienti b: "))
c = int(input("Inserire coefficienti c: "))

print("Equazione: %dx^2 + %dx + %dc" %(a,b,c))
delta = b**2 - 4*a*c;

if(delta>=0):
    x1 = (-1*b + math.sqrt(delta))/(2*a)
    x2 = (-1*b - math.sqrt(delta))/(2*a)
    print("Radice1: %f, radice2: %f" %(x1, x2));
else:
    print("Non ci sono soluzioni reali")