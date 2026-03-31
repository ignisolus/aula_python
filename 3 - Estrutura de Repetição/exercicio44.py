total = 0
precos = {100: 1.2, 101: 1.3, 102: 1.5, 103: 1.2, 104: 1.3, 105: 1.0}
while True:
    cod = int(input("Cód (0 sai): "))
    if cod == 0: break
    qtd = int(input("Qtd: "))
    valor = precos[cod] * qtd
    total += valor
    print(f"Item {cod}: R$ {valor:.2f}")
print(f"Total: R$ {total:.2f}")