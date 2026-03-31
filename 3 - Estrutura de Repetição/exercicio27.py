turmas = int(input("Qtd turmas: "))
soma_alunos = 0
for i in range(turmas):
    alunos = int(input(f"Alunos turma {i+1} (max 40): "))
    while alunos > 40:
        alunos = int(input("Erro. Máximo 40 alunos: "))
    soma_alunos += alunos
print("Média por turma:", soma_alunos / turmas)