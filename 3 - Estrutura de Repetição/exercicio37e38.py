mais_alto = mais_baixo = mais_gordo = mais_magro = 0
h_alto = p_gordo = 0
h_baixo = p_magro = 999
soma_h = soma_p = cont = 0

while True:
    cod = int(input("Código (0 sai): "))
    if cod == 0: break
    h = float(input("Altura: "))
    p = float(input("Peso: "))
    if h > h_alto: h_alto = h; mais_alto = cod
    if h < h_baixo: h_baixo = h; mais_baixo = cod
    if p > p_gordo: p_gordo = p; mais_gordo = cod
    if p < p_magro: p_magro = p; mais_magro = cod
    soma_h += h; soma_p += p; cont += 1
print(f"Alto: {mais_alto} ({h_alto}), Baixo: {mais_baixo} ({h_baixo})")
print(f"Gordo: {mais_gordo} ({p_gordo}), Magro: {mais_magro} ({p_magro})")
print(f"Médias: H {soma_h/cont:.2f}, P {soma_p/cont:.2f}")