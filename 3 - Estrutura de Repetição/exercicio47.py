while True:
    nome = input("Atleta: ")
    if nome == "": break
    saltos = []
    for i in range(5):
        saltos.append(float(input(f"Salto {i+1}: ")))
    
    melhor = max(saltos); pior = min(saltos)
    saltos.remove(melhor); saltos.remove(pior)
    media = sum(saltos)/3
    print(f"Melhor: {melhor}m, Pior: {pior}m, Média: {media:.1f}m")
    print(f"Resultado final: {nome}: {media:.1f}m")