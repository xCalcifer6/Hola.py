# Numeros de Armstrong #

def Narcisista(numero):
  cifras = len(str(numero))
  mysplit = list(str(numero))
  my_list = list()
  for element in mysplit:
    my_list.append(int(element) ** cifras)
  
  sumav = 0
  for element in my_list:
    sumav += element 

  if sumav == numero:
    print("Es ARMSTRONG") 
  else:
    print("No es ARMSTRONG")

Narcisista(153)




