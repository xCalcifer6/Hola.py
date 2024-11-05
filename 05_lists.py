### Lists ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [23, 1.80, "Alvaro", "Espinosa"]

print(my_list)
print(my_other_list)

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

# ADICIONES

my_other_list.append("Skere") #Adicion al final de la lista.
print(my_other_list)

my_other_list.insert(1, "verde") #Adiccion eligiendo posicion.
print(my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list[1] = "verde"
print(my_other_list)

my_other_list.remove("verde")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list) #Borra la lista pero con una copia.

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list = ["banana", "manzana", "pera"]
my_list.sort(reverse = True) # Imprimir la lista descendiente alfabeticamente.
print(my_list)

[print(x) for x in ["banana", "manzana", "pera"]]

my_list.reverse # Imprimir la lista de atras a adelante.
print(my_list)


mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']

fruits = ['apple', 'zanana', 'cherry']

mylist = list(fruits)
print(mylist) # Como copiar una lista forma 2.

mylist = fruits[0:3] # Froma3 de como copiar una lista.(no son necesarios los numeros)


mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']

fruits = ['apple', 'zanana', 'cherry']

mylist += fruits
print(mylist) # Como sumar listas sin crear una adiccional.

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']

fruits = ['apple', 'zanana', 'cherry']

mylist.extend(fruits) # añadir una lista a otra(extend)

print(mylist)

fruits = ('apple', 'banana', 'cherry', "potatoe")
(x, a, *y) = fruits
print(y) # Imprimir a partir de un elemento en adelante.