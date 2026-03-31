votos = [0]*7
total = 0
while True:
    v = int(input("Voto: "))
    if v == 0: break
    if 1 <= v <= 6:
        votos[v] += 1
        total += 1
print(f"1-Jose:{votos[1]}, 2-João:{votos[2]}, 3-Maria:{votos[3]}, 4-Ana:{votos[4]}")
print(f"5-Nulo:{votos[5]}, 6-Branco:{votos[6]}")
print(f"%Nulo: {votos[5]/total*100:.2f}%, %Branco: {votos[6]/total*100:.2f}%")