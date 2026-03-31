n = int(input("Verificar primos até: "))
divisoes = 0
for num in range(2, n + 1):
    primo = True
    for i in range(2, num):
        divisoes += 1
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)
print("Total de divisões:", divisoes)