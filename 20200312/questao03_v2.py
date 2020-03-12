ano = int(input())

m_400 = ano % 400
m_100 = ano % 100
m_4 = ano % 4

if (m_400 == 0) or ((m_4 == 0) and (m_100 != 0)):
  print('sim')
else:
  print('não')