'''
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
'''

num1, num2 = input("Dois valores: ").split()
num1, num2 = int(num1), int(num2)

media_pond = ((num1 * 4) + (num2 * 6)) / 10

print(f"Média ponderada = {media_pond}")