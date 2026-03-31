divida = float(input("Dívida: "))
print("Dívida | Juros | Parcelas | Valor Parcela")
for p in [1, 3, 6, 9, 12]:
    juros_p = 0 if p == 1 else (10 if p == 3 else 15 if p == 6 else 20 if p == 9 else 25)
    v_juros = divida * (juros_p/100)
    v_total = divida + v_juros
    v_parc = v_total / p
    print(f"R$ {v_total:.2f} | {v_juros:.2f} | {p} | R$ {v_parc:.2f}")