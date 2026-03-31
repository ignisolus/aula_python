while True:
    print("Lojas Tabajara")
    total = 0
    cont = 1
    while True:
        preco = float(input(f"Produto {cont}: R$ "))
        if preco == 0: break
        total += preco
        cont += 1
    print(f"Total: R$ {total:.2f}")
    pago = float(input("Dinheiro: R$ "))
    print(f"Troco: R$ {pago - total:.2f}")
    print("--- Próxima Compra ---")