 ## LOOPS ##

# While

my_condition = 0

while my_condition < 20:
    print(my_condition) 
    my_condition += 2 # Incrementa de a (numeros) hasta llegar a la condicion.
else:
    print("mi condicion es mayor o igual que 10")

print("la ejecucion continua")   

my_condition = 0
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecucion")
        break

        print(my_condition)

print("la ejecucion continua")   

# For , funciona con listas, tuplas, sets

my_list = [12, 24, 35, 64, 88, 30, 30]

for element in my_list: # Se reproduce segun la cantidad de elementos en una lista/set/tupla
    print(element)
    if element == 35:
        break
else:
    print("el bucle de mi lista finalizo")

my_list = [12, 24, 35, 64, 88, 30, 30]
for element in my_list:
        print(element)
        if element == 35:
           continue # No se usa casi. Es para saltear.
else:
    print("el bucle de mi lista finalizo")


[print(x) for x in ['apple', 'banana', 'cherry']] # Forma sencilla de loopear lista.