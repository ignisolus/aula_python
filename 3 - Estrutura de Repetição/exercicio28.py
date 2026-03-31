cds = int(input("Quantidade de CDs: "))
total = 0
for i in range(cds):
    total += float(input(f"Valor do CD {i+1}: "))
print("Total investido:", total)
print("Média por CD:", total / cds)