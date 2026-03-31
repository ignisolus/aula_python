l1 = float(input())
l2 = float(input())
l3 = float(input())

if (l1+l2 > l3) and (l1+l3 > l2) and (l2+l3 > l1):
    if l1 == l2 == l3: print("Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3: print("Isósceles")
    else: print("Escaleno")
else:
    print("Não é triângulo")