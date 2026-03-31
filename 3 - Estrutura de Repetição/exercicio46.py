gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
total_alunos = soma_notas = 0
maior = 0; menor = 11

while True:
    acertos = 0
    for i in range(10):
        resp = input(f"Questão {i+1}: ").upper()
        if resp == gabarito[i]: acertos += 1
    if acertos > maior: maior = acertos
    if acertos < menor: menor = acertos
    soma_notas += acertos
    total_alunos += 1
    if input("Outro aluno? (s/n): ") == "n": break
print(f"Maior: {maior}, Menor: {menor}, Total Alunos: {total_alunos}, Média: {soma_notas/total_alunos}")