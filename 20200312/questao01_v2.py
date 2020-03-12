n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if (n1 < n2) and (n1 < n3):
  # n1 é o menor de todos
  if (n2 < n3):
    print(n1, n2, n3)
  else:
    print(n1, n3, n2)
elif (n2 < n3):
  # n1 não é o menor de todos
  # n2 é o menor de todos
  if (n1 < n3):
    print(n2, n1, n3)
  else:
    print(n2, n3, n1)
elif (n1 < n2):
  # n3 é o menor de todos
  print(n3, n1, n2)
else:
  print(n3, n2, n1)