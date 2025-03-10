num = int(input("Inserire numero intero positivo: "))
while (num < 0):
    num = int(input("Inserire numero intero positivo: "))

i = 0;
for val in str(num):
    i += 1

print("Numero cifre: " + str(i))
