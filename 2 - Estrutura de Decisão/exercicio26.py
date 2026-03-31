valor = int(input("Saque (10-600): "))
if 10 <= valor <= 600:
    notas100 = valor // 100
    valor %= 100
    notas50 = valor // 50
    valor %= 50
    notas10 = valor // 10
    valor %= 10
    notas5 = valor // 5
    valor %= 5
    notas1 = valor
    print(f"100:{notas100}, 50:{notas50}, 10:{notas10}, 5:{notas5}, 1:{notas1}")