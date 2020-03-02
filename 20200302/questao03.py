dia, mes, ano = input().split('/')
dia, mes, ano = int(dia), int(mes), int(ano)

dias = dia + mes * 30 + ano * 365

print(dias)