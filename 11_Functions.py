 # Funciones #

def my_function():
    print("esto es una función")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values (5, 7)  

def sum_values_return(first_value, second_value):
    return first_value + second_value

my_result = sum_values_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name}, {surname}")

print_name(name= "Alvaro", surname= "Espinosa")

def print_name_default(name, surname, alias = "Sin Alias"): # Definir un argumento.
    print(f"{name}, {surname}, {alias}")

print_name_default("Alvaro",  "Espinosa")

def print_texts(*text):
    print(text)

print_texts("Hola", "Como estas")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "python", "como estas")


def my_function(*kids): # Si no se conoce cuantos argumentos hay va el * .
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") # EL * sirve si no conocemos los parametros.

def my_function(fname):
  print(fname + " equisde ")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def my_function(x, /):
  print(x)

my_function(x = 3) # ERRPOR, el ,/ sirve para no modificar el argumento.