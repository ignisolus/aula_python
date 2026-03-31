i1 = i2 = i3 = i4 = 0
while True:
    n = int(input("Número: "))
    if n < 0: break
    if n <= 25: i1 += 1
    elif n <= 50: i2 += 1
    elif n <= 75: i3 += 1
    elif n <= 100: i4 += 1
print(f"[0-25]:{i1}, [26-50]:{i2}, [51-75]:{i3}, [76-100]:{i4}")