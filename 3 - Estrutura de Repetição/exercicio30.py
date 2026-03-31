preco = float(input("Preço do pão: "))
print("Panificadora Pão de Ontem - Tabela de preços")
for i in range(1, 51):
    print(f"{i} - R$ {i * preco:.2f}")