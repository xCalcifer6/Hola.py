

def my_funcion(Texto1, Texto2):
  contador_numeral = 0
  suma_textos = 0
  while contador_numeral < 100:
    contador_numeral += 1
    if contador_numeral == 16:
      continue
    elif contador_numeral %3==0:
      print(Texto1)
      suma_textos += 1
    elif contador_numeral %5==0:
      print(Texto2)
      suma_textos += 1
    elif contador_numeral %5==0 and contador_numeral %3==0:
      print(Texto2)
    print(contador_numeral)
  return (suma_textos)

 