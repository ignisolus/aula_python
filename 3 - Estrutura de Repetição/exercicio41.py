soma_veiculos = soma_acid_peq = cont_peq = 0
maior_ind = -1; menor_ind = 99999
cid_maior = cid_menor = 0

for i in range(5):
    cod = int(input("Cód Cidade: "))
    veic = int(input("Veículos: "))
    acid = int(input("Acidentes: "))
    indice = acid / veic
    if indice > maior_ind: maior_ind = indice; cid_maior = cod
    if indice < menor_ind: menor_ind = indice; cid_menor = cod
    soma_veiculos += veic
    if veic < 2000:
        soma_acid_peq += acid
        cont_peq += 1
print(f"Maior índice: {maior_ind} (Cid {cid_maior}), Menor: {menor_ind} (Cid {cid_menor})")
print(f"Média veículos: {soma_veiculos/5}")
print(f"Média acid. cidades pequenas: {soma_acid_peq/cont_peq if cont_peq > 0 else 0}")