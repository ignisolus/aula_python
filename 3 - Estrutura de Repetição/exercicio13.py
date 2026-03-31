base = int(input("Base: "))
exp = int(input("Expoente: "))
resultado = 1
for _ in range(exp):
    resultado = resultado * base
print(resultado)