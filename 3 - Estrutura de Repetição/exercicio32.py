n = int(input("Fatorial de: "))
f = 1
print(f"Fatorial de: {n}")
print(f"{n}! =", end=" ")
for i in range(n, 0, -1):
    f *= i
    print(i, end=" . " if i > 1 else " ")
print(f"= {f}")