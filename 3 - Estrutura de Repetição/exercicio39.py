salario = float(input("Salário inicial (1995): "))
percentual = 0.015
salario += salario * percentual
for ano in range(1997, 2027):
    percentual *= 2
    salario += salario * percentual
print(f"Salário atual: R$ {salario:.2f}")