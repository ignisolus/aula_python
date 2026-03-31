n1 = float(input())
n2 = float(input())
op = input("Operação (+,-,*,/): ")
if op == "+": res = n1 + n2
elif op == "-": res = n1 - n2
elif op == "*": res = n1 * n2
else: res = n1 / n2

info = "Par" if res % 2 == 0 else "Ímpar"
pos = "Positivo" if res >= 0 else "Negativo"
tipo = "Inteiro" if res == int(res) else "Decimal"
print(f"Res: {res} | {info}, {pos}, {tipo}")