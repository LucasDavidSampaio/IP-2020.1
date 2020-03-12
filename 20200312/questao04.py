n1, n2, n3, p = input().split()
n1, n2, n3, p = int(n1), int(n2), int(n3), int(p)

if (n1 < n2) and (n1 < n3):
  # n1 é o menor de todos
  if (n2 < n3):
    v1, v2, v3 = n1, n2, n3
  else:
    v1, v2, v3 = n1, n3, n2
elif (n2 < n3):
  # n1 não é o menor de todos
  # n2 é o menor de todos
  if (n1 < n3):
    v1, v2, v3 = n2, n1, n3
  else:
    v1, v2, v3 = n2, n3, n1
elif (n1 < n2):
  # n3 é o menor de todos
  v1, v2, v3 = n3, n1, n2
else:
  v1, v2, v3 = n3, n2, n1

if (v1 <= 25) and (v2 <= 35) and (v3 <= 55) and (p <= 10):
  print('Ok')
else:
  print('Problema')