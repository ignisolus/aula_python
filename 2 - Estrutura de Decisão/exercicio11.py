p1 = float(input("Preço 1: "))
p2 = float(input("Preço 2: "))
p3 = float(input("Preço 3: "))

if p1 < p2 and p1 < p3:
    print("Compre o primeiro")
elif p2 < p1 and p2 < p3:
    print("Compre o segundo")
else:
    print("Compre o terceiro")