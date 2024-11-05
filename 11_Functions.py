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