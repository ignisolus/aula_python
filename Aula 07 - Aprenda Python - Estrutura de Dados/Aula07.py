leituras = {'quarto':22, 'sala':24,'cozinha':28}

print (leituras, 'Exibindo dados...')

leituras['varanda'] = 25
leituras['cozinha'] = 26
print(leituras)
print(leituras.keys())


carteira = {
    'BBSA3':22.70,
    'PETR4':47.16,
    'VALE3':85.87
}
carteira.get('BBSA')
for ativo, preco in carteira.items():
    print(f'o ativo {ativo} possui preço médio de R$ {preco}')


frase = "Python é legal de mais para pessoas sem laudo! Porque se Python não fosse legal " \
"ele seria chato"

palavras = frase.split()
contagem = {}
for palavra in palavras:
    contagem[palavra]=palavras.count(palavra)

print(contagem)
    




