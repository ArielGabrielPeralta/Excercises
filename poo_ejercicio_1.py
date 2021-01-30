"""Ejercicio 1
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

	Un constructor, donde los datos pueden estar vacíos.
	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
	mostrar(): Muestra los datos de la persona.
	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""

class Persona:
	#Creamos el constructor--------------------------------------
	def __init__(self, nombre, edad, dni):
		self.nombre=nombre
		self.edad=edad
		self.dni=dni

	#Creamos los getters------------------------------------------
	@property
	def nombre(self):
		return self.__nombre

	@property
	def edad(self):
		return self.__edad

	@property
	def dni(self):
		return self.__dni

	#Creamos los setters-------------------------------------------
	@nombre.setter
	def nombre(self, nombre):
		self.__nombre=nombre

	@edad.setter
	def edad(self, edad):
		self.__edad=edad

	@dni.setter
	def dni(self, dni):
		self.__dni=dni

	#Validamos la edad y el dni--------------------------------------
	def validar_edad (self):
		try:
			self.__edad = int(self.__edad)
			if self.__edad <= 0:
				print("Lamento que no tengas la edad necesaria para nacer")
		except ValueError:
			print ("No ingresaste un numero entero")

	def validar_dni(self):
		try:
			self.__dni = int(self.__dni)
		except ValueError:
			print ("No ingresaste un numero entero")

	#Creamos las funciones mostrar y es_mayor_de_edad------------------
	def mostrar(self):
		print("Nombre: "+str(self.__nombre)+"; Edad: "+str(self.__edad)+"; DNI: "+str(self.__dni))

	def es_mayor_de_edad (self):
		try:
			self.__edad = int(self.__edad)
			return self.edad>=18
		except ValueError:
			print ("No ingresaste un numero entero")


"""
p1 = Persona("Juan","45","542318654")
p1.validar_edad()
p1.validar_dni()
p1.mostrar()
print(p1.es_mayor_de_edad())
"""