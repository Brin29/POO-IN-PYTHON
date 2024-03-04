class Personaje:
  # pass marcador de posición para codigo futuro
  # para evitar errores donde no se permite codigo vacio
  # pass
  nombre = "Defecto"
  fuerza = 0
  inteligencia = 0
  defensa = 0
  vida = 0

  # valores con el metodo constructor
  # self argumento que hace referencia a si mismo osea Personaje permite tener acceso a los atributos y metodos this en JavaScript
  def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
    self.nombre = nombre
    self.fuerza = fuerza
    self.inteligencia = inteligencia
    self.defensa = defensa
    self.vida = vida

# Metodo constructor
# instancia de Personaje a mi_personaje
mi_personaje = Personaje()

# Modificando los atributos
mi_personaje.nombre = "Goku"
mi_personaje.fuerza = "97"
mi_personaje.inteligencia = "78"
mi_personaje.defensa = "92"
mi_personaje.vida = 100

print("El nombre del jugador es:", mi_personaje.nombre)
print("La fuerza del jugador es:", mi_personaje.fuerza)
print("La inteligencia  del jugador es:", mi_personaje.inteligencia)
print("La defensa del jugador es:", mi_personaje.defensa)
print("La vida del jugador es:", mi_personaje.vida)