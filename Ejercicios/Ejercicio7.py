"""
Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”. Por tanto:
En la clase “Persona” su método __init__() debe de estar preparado para recibir nombre y apellido.
Además, esta clase , debe tener un método para mostrar nombre_completo() el cual debe mostrar el nombre acompañado del apellido.
La otra clase “Estudiante”, debe de poder heredar de “Persona”, y además recibir los argumentos nombre y edad. 
También la clase “Estudiante”, recibe el valor “carrera”, y además contar con un método mostrar_carrera(). Las dos clases son obligatorias.
"""



class Persona:
    def __init__(self, nombre, apellido):
        self.nombre_completo = f'{nombre}, {apellido}'
        self.apellido = apellido

padre = Persona("Roberto", "Garcia")
print(padre.nombre_completo)

class Estudiante:
    def __init__(self, apellido, edad, carrera, nombre = "Tomas"):
        self.full_name = f'{nombre}, {apellido}'
        self.carrera = carrera
    def mostrar_carrera(self):
        print(f"{self.full_name} estudia {self.carrera}")


hijo = Estudiante(padre.apellido, 21, "Quimico") 
print(hijo.full_name)        

hijo.mostrar_carrera()