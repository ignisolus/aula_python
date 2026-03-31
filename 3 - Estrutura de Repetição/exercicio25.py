n_pessoas = int(input("Nº de pessoas: "))
soma = 0
for i in range(n_pessoas):
    soma += int(input("Idade: "))
media = soma / n_pessoas
if media <= 25: print("Jovem")
elif media <= 60: print("Adulta")
else: print("Idosa")