## LAMBDAS ##
# Son como funciones pero mas resumidas, sin nombres, se les puede asignar una variable #

suma_variables = lambda first_value, second_value: first_value + second_value
print(suma_variables(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value + 3
print(multiply_values(3, 5))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(3, 6))