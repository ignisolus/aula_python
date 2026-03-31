t = int(input("Tabuada de: "))
ini = int(input("Começar por: "))
fim = int(input("Terminar em: "))
if fim < ini:
    print("Erro: fim menor que início")
else:
    for i in range(ini, fim + 1):
        print(f"{t} X {i} = {t*i}")