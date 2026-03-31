valor_hora = float(input("Ganha por hora: "))
horas_trabalhadas = float(input("Horas no mês: "))

bruto = valor_hora * horas_trabalhadas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

print("+ Salário Bruto : R$", bruto)
print("- IR (11%) : R$", ir)
print("- INSS (8%) : R$", inss)
print("- Sindicato (5%) : R$", sindicato)
print("= Salário Liquido : R$", liquido)