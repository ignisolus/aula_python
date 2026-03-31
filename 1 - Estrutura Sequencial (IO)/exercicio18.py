arquivo_mb = float(input("Tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Velocidade da internet (Mbps): "))

velocidade_mb_segundo = velocidade_mbps / 8
tempo_segundos = arquivo_mb / velocidade_mb_segundo
tempo_minutos = tempo_segundos / 60

print("Tempo aproximado em minutos:", tempo_minutos)