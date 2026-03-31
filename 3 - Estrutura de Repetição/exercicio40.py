alto_cod = baixo_cod = 0
alto_h = 0
baixo_h = 999
for i in range(10):
    cod = int(input("Cód aluno: "))
    h = float(input("Altura: "))
    if h > alto_h: alto_h = h; alto_cod = cod
    if h < baixo_h: baixo_h = h; baixo_cod = cod
print(f"Mais alto: {alto_cod} com {alto_h}cm")
print(f"Mais baixo: {baixo_cod} com {baixo_h}cm")