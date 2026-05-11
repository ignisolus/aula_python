#Exercício 1
def potencia(numero, expoente):
    return numero ** expoente

# Exemplo:
resultado = potencia(2, 3)
print(f"O resultado é: {resultado}")

#Exercício 2
def formatar_data(dia, mes, ano):
    return f"{dia:02d}/{mes:02d}/{ano:04d}"

# Exemplo:
data_formatada = formatar_data(5, 5, 2026)
print(data_formatada)

#Exercício 3
def formatar_mensagem(mensagem, maiuscula=True):
    if maiuscula:
        return mensagem.upper()
    else:
        return mensagem.lower()

# Exemplo:
print(formatar_mensagem("Python é vida!"))
print(formatar_mensagem("Python é vida!", False))

#Exercício 4
def fatorial(n):
    if n < 0:
        return "Não existe fatorial de número negativo"
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Exemplo:
print(fatorial(5))

#Exercício 5
def calcular_imc(nome, peso, idade, altura):
    imc = peso / (altura ** 2)
    return imc

# Exemplo:
meu_imc = calcular_imc("Rodrigo", 80.0, 30, 1.80)
print(f"O IMC calculado é: {meu_imc:.2f}")

#Exercícios 6 e 7
lista_de_frutas = []

def pegar_frutas():
    for i in range(3):
        fruta = input(f"Digite o nome da {i+1}ª fruta: ")
        lista_de_frutas.append(fruta)

def exibir_frutas(lista):
    for fruta in lista:
        print(f"Fruta: {fruta}")

# Exemplo
frutas_teste = ["Pera", "Maçã", "Cenoura"]
exibir_frutas(frutas_teste)




