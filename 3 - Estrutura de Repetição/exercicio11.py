n1 = int(input("Início: "))
n2 = int(input("Fim: "))
soma = 0
for i in range(n1 + 1, n2):
    print(i)
    soma += i
print("Soma:", soma)