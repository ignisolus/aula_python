tipo = input("Carne (File/Alcatra/Picanha): ")
kg = float(input("Kg: "))
cartao = input("Cartão Tabajara? (s/n): ")

if tipo == "File":
    preco = 4.90 if kg <= 5 else 5.80
elif tipo == "Alcatra":
    preco = 5.90 if kg <= 5 else 6.80
else:
    preco = 6.90 if kg <= 5 else 7.80

bruto = kg * preco
desc = bruto * 0.05 if cartao == "s" else 0
print(f"Tipo: {tipo} | Qtd: {kg}kg | Total: {bruto} | Desc: {desc} | Pagar: {bruto-desc}")