# Variables

my_string_variable = "Random Variable"
print (my_string_variable)

my_int_variable = 5
print(my_int_variable)

colores = ['rojo', 'verde', 'amarillo']

longitud_colores = len(colores)

print(f'la lista de colores contiene {longitud_colores}')

# Concatenacion de variables en un print

print(my_string_variable, my_int_variable, longitud_colores)

# Variables en una sola linea

conteo = str(10)
print(type(conteo))

x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x) # Convierte la variable de dentro de la funcion a global.

x = 5
x = float(x) # Pasa un numero a float


x = 9
print(f'The price is {x:.4f} dollars') # .4f es para añadir la cantidad de 0 que quieras.
                                       # x: para devolver el contedido de la variable

print(f'The price is {2 + 3} dollars')


print(bool("a")) # Devuelve True si adentro hay algo.

print(bool(0)) # 0 es Negativo y 1 Positivo, devuelve False o True.