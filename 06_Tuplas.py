# Tuplas #

my_tuple = tuple()
my_other_tuple = ()

my_tuple = ("Alvaro", "Espinosa", "1.81", 23)
my_other_tuple = (35, 26, 27, 80)


my_last_tuple = my_tuple + my_other_tuple
print(my_last_tuple)

print(my_last_tuple[3:5]) #printear cosas especificas.

# Para modificar una tupla hay que pasarla a list. #

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = 24
my_tuple.insert(1, "Alvarito")

my_tuple = tuple(my_tuple)
print(type(my_tuple))
