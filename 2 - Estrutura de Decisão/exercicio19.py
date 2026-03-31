n1 = float(input())
n2 = float(input())
m = (n1 + n2) / 2

if m >= 9: conc = "A"
elif m >= 7.5: conc = "B"
elif m >= 6: conc = "C"
elif m >= 4: conc = "D"
else: conc = "E"

status = "APROVADO" if conc in "ABC" else "REPROVADO"
print(f"Notas: {n1}, {n2} | Média: {m} | Conceito: {conc} | {status}")