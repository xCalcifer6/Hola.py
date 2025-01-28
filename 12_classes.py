    ### CLASSES ####

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person("Alvaro", "Espinosa")

print(f"{my_person.name} {my_person.surname}")



class Person:
    def __init__(self, name, surname, alias = "sin alias"):
        self.full_name = f"{name} {surname}"

    def walk (self):
        print(f"{self.full_name} Está caminando")

my_person = Person("Alvaro", "Espinosa")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Alvaro", "Espinosa", "Cruz")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self): # Devuelve nombre y apellido.
    return f"{self.name}({self.age})" 

p1 = Person("John", 36)

print(p1)


class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage() # El Super() sirve para ahorrar comandos largos o no tener que repetirlos.



