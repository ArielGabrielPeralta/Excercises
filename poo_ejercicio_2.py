""" Ejercicio 2:
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""

from poo_ejercicio_1 import Persona

#Clase que representa la cuenta de una persona.
class Cuenta(Persona):

	#Constructor de Cuenta-------------------------------------------------------------------------------------------
    def __init__(self,titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    #Es un plus que agregué paraque  se pueda imprimir  sin la funcion "mostrar()" ----------------------------------
    def __str__(self):
        cadena = str(self.__titular) + ", Cantidad:" + str(self.__cantidad)
        return cadena

    #getters---------------------------------------------------------------------------------------------------------
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    #setters----------------------------------------------------------------------------------------------------------
    @titular.setter
    def titular(self,titular):
        self.__titular=titular

    #metodos----------------------------------------------------------------------------------------------------------
    #mostrar(): Muestra los datos de la cuenta.
    def mostrar(self):
        return "Cuenta\n"+"Titular:"+self.titular.mostrar()+" - Cantidad: "+str(self.__cantidad)

    #ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    #retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

"""
p1 = Persona("Juan",45,542318654)
c1=Cuenta(p1,45.6)
print(c1)
c1.ingresar(-14.4)
print(c1)
c1.retirar(20.8)
print(c1)
"""