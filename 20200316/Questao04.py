qtde = 0

for i in range(6):
    idade = int(input())

    if (idade == 16) or (idade == 17) or (idade >= 70):
        qtde += 1

print(qtde)
