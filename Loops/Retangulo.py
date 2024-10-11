
linha = 4
coluna = 4
simbolo = '*'
for l in range(linha):
    for c in range(coluna):
        print(simbolo, end=" ")
    print()

print(" melim ".center(30,"-"))

altura = 5
for a in range(1, altura+1):
    print("*" * a)
