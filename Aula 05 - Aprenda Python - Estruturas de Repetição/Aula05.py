#exercicio 1#
frase = input("Digite uma frase: ").lower()
total_vogais = 0
for letra in frase:
    if letra in "aeiou":
        total_vogais += 1
print(total_vogais)

#exercicio 2#
for i in range(48, 0, -3):
    print(i)

#exercicio 3#
convidados = ["Alice", "Bob", "Carlos", "Diana", "Eduardo"]
numero = 1
for nome in convidados:
    print(f"{numero}. {nome}")
    numero += 1

#exercicio 4#
for i in range(5):
    num = int(input("Digite um número: "))
    if num == 0:
        print("Processamento interrompido")
        break
else:
    print("Sequência processada com sucesso")

#exercicio 5#
precos = [10.50, 150.00, 45.00, 210.90, 85.00, 300.00]
produtos_premium = []
for preco in precos:
    if preco > 100.00:
        produtos_premium.append(preco)
print(produtos_premium)