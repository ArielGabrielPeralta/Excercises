"""Ejercicio 3:
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior. 
Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
Construye los siguientes métodos para la clase:

Un constructor.
Los setters y getters para el nuevo atributo.
En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() 
que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
Además la retirada de dinero sólo se podrá hacer si el titular es válido.
El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir."""

from poo_ejercicio_1 import Persona
from poo_ejercicio_2 import Cuenta

class CuentaJoven (Cuenta):
        #constructor---------------------------------------------------------------------------------------------------------------
        def __init__(self, titular , cantidad = 0, bonificacion = 0):
                self.__titular = titular
                self.__cantidad = cantidad
                self.__bonificacion = bonificacion

        def __str__(self):
                cadena = str(self.__titular) + ", Cantidad: " + str(self.__cantidad) + ", Bonificación: %" + str(self.__bonificacion)
                return cadena

        #getters--------------------------------------------------------------------------------------------------------------------
        @property
        def titular(self):
                return self.__titular

        @property
        def cantidad(self):
                return self.__cantidad
        
        @property
        def bonificacion(self):
                return self.__bonificacion

        #setters---------------------------------------------------------------------------------------------------------------------
        @titular.setter
        def titular(self, titular):
                self.__titular

        @bonificacion.setter
        def bonificacion(self,bonificacion):
                self.__bonificacion = bonificacion

        #metodos--------------------------------------------------------------------------------------------------------------------
        def esTitularValido(self):
                return  self.titular.edad >= 18 and self.titular.edad <= 25

        def mostrar(self):
                if self.esTitularValido():
                        print("Cuenta Joven. Tenes una bonificacion del %" + str(self.bonificacion))
                else:
                        print("No es una Cuenta Joven")

        def retirar(self,cantidad):
                if not self.esTitularValido():
                        print ("No puesdes retirar el dinero. titular no válido")
                elif cantidad > 0:
                        super().retirar(cantidad)

"""
p1 = Persona("Juan",24,542318654)
cj1= CuentaJoven(p1, 45.14, 54)
print(cj1)
print(cj1.esTitularValido())
cj1.mostrar()
"""