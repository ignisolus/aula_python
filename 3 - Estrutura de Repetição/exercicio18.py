n_vezes = int(input("Quantos números? "))
lista = []
for i in range(n_vezes):
    num = float(input("Valor: "))
    lista.append(num)
print("Menor:", min(lista))
print("Maior:", max(lista))
print("Soma:", sum(lista))