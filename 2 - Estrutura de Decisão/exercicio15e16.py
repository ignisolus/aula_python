salario = float(input("Salário: "))
if salario <= 280:
    porcentagem = 20
elif salario <= 700:
    porcentagem = 15
elif salario <= 1500:
    porcentagem = 10
else:
    porcentagem = 5

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print("Antes:", salario)
print("Percentual:", porcentagem, "%")
print("Valor aumento:", aumento)
print("Novo salário:", novo_salario)