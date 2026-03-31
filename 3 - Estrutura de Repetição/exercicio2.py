usuario = input("Usuário: ")
senha = input("Senha: ")
while senha == usuario:
    print("Erro: a senha não pode ser igual ao nome de usuário.")
    usuario = input("Usuário: ")
    senha = input("Senha: ")