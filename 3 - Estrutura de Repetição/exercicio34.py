num = int(input("Número: "))
primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
if primo and num > 1: print("É primo")
else: print("Não é primo")