lista_temp = []
while True:
    t = input("Temp (vazio p/ sair): ")
    if t == "": break
    lista_temp.append(float(t))
print("Menor:", min(lista_temp))
print("Maior:", max(lista_temp))
print("Média:", sum(lista_temp)/len(lista_temp))