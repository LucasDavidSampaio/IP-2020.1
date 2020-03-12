ano = int(input())

c_400 = ano % 400 == 0
c_100 = ano % 100 == 0
c_4 = ano % 4 != 0

if (c_400) or ((c_4) and (c_100)):
  print('sim')
else:
  print('não')