
"""
 * Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (lista de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 """

monedas = [5, 10, 50, 100, 200]

productos = {"0":"pepsi", "1":"papitas", "2":"chocolate", "3":"chupetines", "4":"coca", "5":"juguito"}
precios = [20, 15, 10, 20, 5, 10]

producto_seleccionado = input("Elija un producto: ")
print(f'{productos[producto_seleccionado]}: ${precios[int(producto_seleccionado)]}')
pagar = input("Ingrese el dinero: $")
if int(pagar) == precios[int(producto_seleccionado)]:
  print("Retire su producto.")
elif int(pagar) > precios[int(producto_seleccionado)]:
  cambio = int(pagar) - precios[int(producto_seleccionado)]
  print(cambio)
  print("Retire su cambio.")  
elif int(pagar) < precios[int(producto_seleccionado)]:
  print(pagar)
  print("Dinero Insuficiente.") 

