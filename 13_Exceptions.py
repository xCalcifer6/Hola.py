    ### Exceptions // Excepciones ###

NumberOne = 1
NumberTwo = 2
NumberTwo = "2"

try:
    print(NumberOne + NumberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally


try:
    print(NumberOne + NumberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Errores por tipo.

try:
    print(NumberOne + NumberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")



