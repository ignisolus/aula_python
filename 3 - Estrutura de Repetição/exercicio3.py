nome = input("Nome: ")
while len(nome) <= 3:
    nome = input("Nome (mais de 3 caracteres): ")

idade = int(input("Idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade (0 a 150): "))

salario = float(input("Salário: "))
while salario <= 0:
    salario = float(input("Salário (maior que 0): "))

sexo = input("Sexo (f/m): ").lower()
while sexo not in ['f', 'm']:
    sexo = input("Sexo (f/m): ").lower()

estado_civil = input("Estado Civil (s/c/v/d): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    estado_civil = input("Estado Civil (s/c/v/d): ").lower()