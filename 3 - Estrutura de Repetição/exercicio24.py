n_notas = int(input("Quantas notas? "))
soma = 0
for i in range(n_notas):
    soma += float(input("Nota: "))
print("Média:", soma / n_notas)