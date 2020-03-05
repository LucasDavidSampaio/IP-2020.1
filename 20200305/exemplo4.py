idade = int(input('Idade: '))

if (idade <= 15):
  print('Não pode')
else:
  if (idade <= 17):
    print('Pode')
  else:
    if (idade <= 70):
      print('Obrigatório')
    else:
      print('Pode')

'''
- Artigo sobre a obrigatoriedade do voto
http://www.tse.jus.br/imprensa/noticias-tse/2018/Abril/eleicoes-2018-saiba-para-quem-o-voto-e-facultativo-e-obrigatorio
'''