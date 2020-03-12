media, freq = input().split()
media, freq = int(media), int(freq)

if (media == 100) or ((media >= 70) and (freq >= 75)):
  print('aprovado')
else:
  print('reprovado')