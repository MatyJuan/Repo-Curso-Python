# """
# Ejercicio POO/OOP (Programacion Orientada a objetos):
# https://ellibrodepython.com/programacion-orientada-a-objetos-python
# """

#Ejercicio 1

class Persona:
  def __init__(self):
      self.__nombre = None
      self.__edad = None
      self.__dni = None

  @property
  def nombre(self):
    return self.__nombre

  @nombre.getter
  def nombre(self):
    return self.__nombre

  @nombre.setter
  def nombre(self,valor):
    if type(valor) == str:
      self.__nombre = valor
    else:
      print("Debe ingresar un nombre válido")
      

  @property
  def edad(self):
    return self.__edad

  @edad.getter
  def edad(self):
    return self.__edad

  @edad.setter
  def edad(self,valor):
    if type(valor) == int:
      self.__edad = valor
    else:
      print("Debe ingresar una edad válida")

  @property
  def dni(self):
    return self.__dni

  @dni.getter
  def dni(self):
    return self.__dni

  @dni.setter
  def dni(self,valor):
    if type(valor) == int:
      self.__dni = valor
    else:
      print("Debe ingresar un dni válido")

  def mostrar(self):
    if persona.nombre:
      print(persona.nombre)
    if persona.edad:
      print(persona.edad)
    if persona.dni:
      print(persona.dni)

  def mayor_de_edad(self):
    return True if self.edad >=18 else False
    
persona = Persona()  
#Setter  
persona.nombre = "Matias"
persona.edad = 23
persona.dni = 42057407

persona.mostrar()
print(persona.mayor_de_edad())
    
    

# """
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
# Construye los siguientes métodos para la clase:
#     - Un constructor, donde los datos pueden estar vacíos.
#     - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#     - mostrar(): Muestra los datos de la persona.
#     - es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
# """


#Ejercicio 2
# """
# Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
#     titular (que es una persona)
#     cantidad (puede tener decimales)
# El titular será obligatorio y la cantidad es opcional. 
# Construye los siguientes métodos para la clase:
#     - Un constructor, donde los datos pueden estar vacíos.
#     - Los setters y getters para cada uno de los atributos.
#       El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#     - mostrar(): Muestra los datos de la cuenta.
#     - ingresar(cantidad): se ingresa una cantidad a la cuenta.
#       si la cantidad introducida es negativa, no se hará nada.
#     - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
# """
# class Cuenta:
#   def __init__(self, titular , cantidad ):
# # #Ejercicio 3
# # """
# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que 
# deriva de la anterior.
# Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación
# que estará expresada en tanto por ciento.

# Construye los siguientes métodos para la clase:
#     - Un constructor.
#     - Los setters y getters para el nuevo atributo.
#     - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad.
#       Por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad
#       pero menor de 25 años y falso en caso contrario.
#     - Además la retirada de dinero sólo se podrá hacer si el titular es válido.
#     - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
#     - Piensa los métodos heredados de la clase madre que hay que reescribir.
# """