data = input("dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

valida = False
if mes >= 1 and mes <= 12:
    if mes in [1,3,5,7,8,10,12] and dia <= 31: valida = True
    elif mes in [4,6,9,11] and dia <= 30: valida = True
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia <= 29: valida = True
        elif dia <= 28: valida = True

if valida: print("Válida")
else: print("Inválida")