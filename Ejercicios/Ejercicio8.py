## CLASES ##

class Perro:
  def __init__(self, color = "marron", raza = "chihuahua", nombre = "Tobi"):
    self.perro_completo = f"{color} {raza} {nombre}"

  def llamar_perro(self):
      print(self.perro_completo)

my_perro = Perro().llamar_perro()

