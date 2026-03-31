litros = float(input("Litros: "))
tipo = input("A ou G: ").upper()
if tipo == "A":
    preco = 1.90
    desc = 0.03 if litros <= 20 else 0.05
else:
    preco = 2.50
    desc = 0.04 if litros <= 20 else 0.06
total = litros * (preco * (1 - desc))
print(total)