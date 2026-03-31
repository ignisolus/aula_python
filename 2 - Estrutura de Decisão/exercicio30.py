p1 = input("Telefonou? ")
p2 = input("Local? ")
p3 = input("Mora perto? ")
p4 = input("Devia? ")
p5 = input("Trabalhou? ")

soma = 0
for p in [p1, p2, p3, p4, p5]:
    if p.lower() == "sim": soma += 1

if soma == 2: print("Suspeita")
elif 3 <= soma <= 4: print("Cúmplice")
elif soma == 5: print("Assassino")
else: print("Inocente")