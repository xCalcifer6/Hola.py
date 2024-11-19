  ## SETS ##

my_set = set()
my_other_set = {} #Inicialmente es un diccionario.      

print((type)(my_set))
print((type)(my_other_set))

my_other_set = {"Alvaro", "Espinosa", 23}
print((type)(my_other_set))

my_other_set.add("Poste")
print(my_other_set) # Un set no es una estructura ordenada.

my_other_set.add("Poste") # Un set no repite 
print(my_other_set)

print("Alvaro" in my_other_set)
print("Skere" in my_other_set) # Asi verificamos si esta en el set o no.

my_set = {"Bmx", "Computadora", "Python"}

my_new_set = my_other_set.union(my_set)
print(my_new_set)

print(my_new_set.difference(my_set)) #Diferencias en sets

cuarto_set = {"Tomate", "Pera", "Palta"} 
quinto_set = {"Banana", "Pera", "Ananá"}
sexto_set = quinto_set.intersection(cuarto_set)
print(sexto_set) # Encuentra el punto en comun entre los sets.

sexto_set = cuarto_set.isdisjoint(quinto_set)
print(sexto_set) # Devuelve True si no hay coincidencias en ambos sets.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits) # Como updatear un set.

fruits.remove, fruits.discard # Remover items de un set.

fruits.clear # Borrar todos los items de un set.


set2 = {"asd, xd"}
set3 = {"xd"}

set1 = set2 | set3 # Como sumar sets en un nuevo set.

set2.intersection(set3)
print()
