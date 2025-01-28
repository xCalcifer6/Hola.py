 ## FUNCIONES DE ORDEN SUPERIOR ##

# Son funciones que trabajan con funciones.

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def suma_dos_valores(one_value, two_value, f_sum):
    return f_sum(one_value + two_value)

print(suma_dos_valores(2, 3, sum_one))
print(suma_dos_valores(2, 3, sum_five))

## CLOSURES ###

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(10))

## Funciones Superiores Del Sistema ##

numbers = [2, 4, 6, 8, 60, 40, 5, 50]

## MAP ##
# Recorre un parametro y cumple la funcion #

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

## FILTER ##
# Filtra el parametro acorde a la funcion, pide True o False ##

def filter_diez(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_diez, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

## REDUCE ##
# Trabaja tomando el resultado de la suma de los primeros dos valores ##

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))