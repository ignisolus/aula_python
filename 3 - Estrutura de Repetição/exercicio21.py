n = int(input("Número: "))
mult = 0
for i in range(2, n):
    if n % i == 0:
        mult += 1
if mult == 0 and n > 1:
    print("É primo")
else:
    print("Não é primo")