valor = int(input("Valor: "))

c100 = valor // 100
valor = valor % 100

c50 = valor // 50
valor = valor % 50

c20 = valor // 20
valor = valor % 20

c10 = valor // 10
valor = valor % 10

c5 = valor // 5
valor = valor % 5

c2 = valor // 2
c1 = valor % 2

print(f"{c100} cédulas de R$ 100,00")
print(f"{c50} cédulas de R$ 50,00")
print(f"{c20} cédulas de R$ 20,00")
print(f"{c10} cédulas de R$ 10,00")
print(f"{c5} cédulas de R$ 5,00")
print(f"{c2} cédulas de R$ 2,00")
print(f"{c1} cédulas de R$ 1,00")