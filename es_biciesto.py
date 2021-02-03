def es_biciesto(anio):
    """
    La función recibirá como parametro el año y nos retornará si es biciesto o no con un valor booleano.
    """
    biciesto = False                            #Inicializamos la variable "biciesto" en "False".
    if anio % 4 == 0 and not anio % 100 == 0:   #Si el modulo de "anio" sobre 4 es igual a 0 y el modulo de "anio" sobre 100 no es igual a 0.
        biciesto = True                             #La variable "biciesto" es "True"
    if anio % 400 == 0:                         #Si el modulo de "anio" sobre 400 es igual a 0.
        biciesto = True                             #La variable "biciesto" es "True"
    return biciesto                             #Retornamos biciesto

"""
def main():
    anio = int(input("ingresa un año: "))
    if es_biciesto(anio):
        print("Es biciesto")
    else:
        print ("No es biciesto")
main()
"""
