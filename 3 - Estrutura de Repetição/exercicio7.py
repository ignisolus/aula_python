maior = float(input("Número 1: "))
for i in range(4):
    n = float(input(f"Número {i+2}: "))
    if n > maior:
        maior = n
print("Maior:", maior)