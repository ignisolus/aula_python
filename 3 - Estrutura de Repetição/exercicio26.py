eleitores = int(input("Total eleitores: "))
c1 = c2 = c3 = 0
for i in range(eleitores):
    voto = input("Voto (1, 2 ou 3): ")
    if voto == '1': c1 += 1
    elif voto == '2': c2 += 1
    elif voto == '3': c3 += 1
print(f"Candidato 1: {c1}\nCandidato 2: {c2}\nCandidato 3: {c3}")