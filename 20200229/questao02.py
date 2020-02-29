n1, n2 = input().split()
n1, n2 = int(n1), int(n2)

'''
aux = n1
n1 = n2
n2 = aux
'''

n1, n2 = n2, n1

print(n1, n2)