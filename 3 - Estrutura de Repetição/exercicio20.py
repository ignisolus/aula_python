while True:
    n = int(input("Fatorial (positivo < 16): "))
    if n < 0 or n >= 16:
        break
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f)