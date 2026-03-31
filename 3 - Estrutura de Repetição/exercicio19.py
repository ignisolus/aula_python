n_vezes = int(input("Quantos números? "))
lista = []
for i in range(n_vezes):
    num = float(input("Valor (0-1000): "))
    while num < 0 or num > 1000:
        num = float(input("Incorreto. Valor (0-1000): "))
    lista.append(num)
print("Menor:", min(lista), "Maior:", max(lista), "Soma:", sum(lista))