class Personaje:
  # nombre = "Defecto"
  # fuerza = 0
  # inteligencia = 0
  # defensa = 0
  # vida = 0

  # valores con el metodo constructor
  # self argumento que hace referencia a si mismo osea Personaje permite tener acceso a los atributos y metodos this en JavaScript
  # con self estamos indicando que atributos inicializar al momento de crearse
  # Esta modificando los atributos al momento de crearlos
  def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
    self.nombre = nombre
    self.fuerza = fuerza
    self.inteligencia = inteligencia
    self.defensa = defensa
    self.vida = vida

  # Metodo de estado del objeto
  def atributos(self):
    print(self.nombre, ":", sep="")
    print(" - Fuerza", self.fuerza)
    print(" - Inteligencia", self.inteligencia)
    print(" - Defensa", self.defensa)
    print(" - Vida", self.vida)
    
  # aumentar valores
  def subir_nivel(self, fuerza, inteligencia, defensa):
    self.fuerza = self.fuerza + fuerza
    self.inteligencia = self.inteligencia + inteligencia
    self.defensa = self.defensa + defensa

  def esta_vivo(self):
    # Verdadero o falso
    return self.vida > 0
  
  # si esta muerto
  def morir(self):
    self.vida = 0
    print(self.nombre, "Ha Muerto")
    
  def daño(self, enemigo):
    return self.fuerza - enemigo.defensa
  
  def atacar(self, enemigo):
    daño = self.daño(enemigo)
    enemigo.vida = enemigo.vida - daño
    print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
    
# Metodo constructor
# instancia de Personaje a mi_personaje
mi_personaje = Personaje("Vegeta", 93, 91, 87, 100)
mi_personaje.atributos()
mi_personaje.subir_nivel(2, 1, 5)
mi_personaje.atributos()
print(mi_personaje.esta_vivo())
mi_personaje.morir()
mi_personaje.atributos()

mi_oponente = Personaje("Goku", 95, 76, 94, 100)
print(mi_personaje.daño(mi_oponente))
print(mi_oponente.daño(mi_personaje))