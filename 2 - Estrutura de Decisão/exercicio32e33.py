morangos = float(input("Kg Morango: "))
macas = float(input("Kg Maçã: "))

p_morango = 2.50 if morangos <= 5 else 2.20
p_maca = 1.80 if macas <= 5 else 1.50

total_rs = (morangos * p_morango) + (macas * p_maca)
if (morangos + macas > 8) or (total_rs > 25):
    total_rs *= 0.90
print(total_rs)