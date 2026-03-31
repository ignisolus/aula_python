while True:
    nome = input("Atleta: ")
    if nome == "": break
    notas = []
    for i in range(7):
        notas.append(float(input(f"Nota: ")))
    melhor = max(notas); pior = min(notas)
    notas.remove(melhor); notas.remove(pior)
    media = sum(notas)/5
    print(f"Melhor: {melhor}, Pior: {pior}, Média: {media:.2f}")

#inverter número
    n = int(input("Número: "))
print(str(n)[::-1])

#séries S e H
n = int(input("Termos: "))
s = 0; m = 1
for i in range(1, n + 1):
    s += i / m
    m += 2
print("Soma S:", s)

h = 0
for i in range(1, n + 1):
    h += 1 / i
print("Soma H:", h)