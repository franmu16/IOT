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