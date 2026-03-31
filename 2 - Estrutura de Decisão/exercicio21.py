a = float(input("A: "))
if a == 0:
    print("Encerrado")
else:
    b = float(input("B: "))
    c = float(input("C: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Sem raízes reais")
    elif delta == 0:
        raiz = -b / (2*a)
        print("Uma raiz:", raiz)
    else:
        r1 = (-b + delta**0.5) / (2*a)
        r2 = (-b - delta**0.5) / (2*a)
        print("Raízes:", r1, r2)