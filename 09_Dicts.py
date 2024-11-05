  ## Dicts o diccionarios ##
## Son estructuras con clave y valor ##

my_dict = dict()
my_other_dict = {}

my_other_dict = {"Nombre":"Alvaro", "Apellido":"Espinosa", "Edad": 23}

my_dict = {
"Nombre": "Alvaro",
"Edad": 18,
"Estatura":1.81,
"Lenguajes": {"Python", "Java"},
6: "Numero Favorito"
}
print(my_dict)
print(my_other_dict)

print(my_dict["Nombre"])

my_dict["Nombre"] = "Cruz" # Asi se actualiza una clave de diccionario.
print(my_dict["Nombre"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys((my_dict)) 
print(my_new_dict) # Diccionario que mantiene las claves sin valores.
