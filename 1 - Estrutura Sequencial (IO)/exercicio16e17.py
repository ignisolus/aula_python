#16

metros = float(input("Metros quadrados: "))
litros = metros / 3
latas = litros / 18

if latas > int(latas):
    latas = int(latas) + 1
else:
    latas = int(latas)

preco = latas * 80
print("Latas:", latas)
print("Preço: R$", preco)


#16 e 17

area = float(input("Área a ser pintada: "))
litros_necessarios = area / 6

# Apenas latas
latas_sozinhase = litros_necessarios / 18
if latas_sozinhase > int(latas_sozinhase):
    latas_sozinhase = int(latas_sozinhase) + 1
print("Apenas latas:", int(latas_sozinhase), "Preço: R$", latas_sozinhase * 80)

# Apenas galões
galoes_sozinhos = litros_necessarios / 3.6
if galoes_sozinhos > int(galoes_sozinhos):
    galoes_sozinhos = int(galoes_sozinhos) + 1
print("Apenas galões:", int(galoes_sozinhos), "Preço: R$", galoes_sozinhos * 25)

# Mistura
litros_folga = litros_necessarios * 1.1
latas_misto = int(litros_folga / 18)
resto = litros_folga % 18
galoes_misto = resto / 3.6
if galoes_misto > int(galoes_misto):
    galoes_misto = int(galoes_misto) + 1

custo_misto = (latas_misto * 80) + (int(galoes_misto) * 25)
print("Misto -> Latas:", latas_misto, "Galões:", int(galoes_misto), "Preço: R$", custo_misto)