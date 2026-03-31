valor_hora = float(input("Valor hora: "))
horas = float(input("Horas: "))
bruto = valor_hora * horas

if bruto <= 900:
    ir = 0
    p_ir = 0
elif bruto <= 1500:
    ir = bruto * 0.05
    p_ir = 5
elif bruto <= 2500:
    ir = bruto * 0.10
    p_ir = 10
else:
    ir = bruto * 0.20
    p_ir = 20

inss = bruto * 0.10
fgts = bruto * 0.11
total_desc = ir + inss
liquido = bruto - total_desc

print(f"Salário Bruto: R$ {bruto}")
print(f"(-) IR ({p_ir}%): R$ {ir}")
print(f"(-) INSS (10%): R$ {inss}")
print(f"FGTS (11%): R$ {fgts}")
print(f"Total de descontos: R$ {total_desc}")
print(f"Salário Liquido: R$ {liquido}")