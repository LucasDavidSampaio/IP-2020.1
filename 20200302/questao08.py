notas, moedas = input().split('.')
notas, moedas = int(notas), int(moedas)

c100 = notas // 100
notas %= 100

c50 = notas // 50
notas %= 50

c20 = notas // 20
notas %= 20

c10 = notas // 10
notas %= 10

c5 = notas // 5
notas %= 5

c2 = notas // 2

m1 = notas % 2

m50 = moedas // 50
moedas %= 50

m25 = moedas // 25
moedas %= 25

m10 = moedas // 10
moedas %= 10

m5 = moedas // 5

m01 = moedas % 5

print('NOTAS:')
print(f'{c100} nota(s) de R$ 100.00')
print(f'{c50} nota(s) de R$ 50.00')
print(f'{c20} nota(s) de R$ 20.00')
print(f'{c10} nota(s) de R$ 10.00')
print(f'{c5} nota(s) de R$ 5.00')
print(f'{c2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{m1} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m5} moeda(s) de R$ 0.05')
print(f'{m01} moeda(s) de R$ 0.01')
