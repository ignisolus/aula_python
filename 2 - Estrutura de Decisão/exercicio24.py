num = int(input("Número < 1000: "))
c = num // 100
d = (num % 100) // 10
u = num % 10
print(f"{c} centenas, {d} dezenas e {u} unidades")