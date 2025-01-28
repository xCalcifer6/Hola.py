## CLASES Y FUNCIONES DE ORDEN SUPERIOR, EJERCICIO ##


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def mayor_edad(self):
        if self.age > 18:
            return True
        return False
    
p1 = Person("Claudio", 16)
print(p1.mayor_edad())
