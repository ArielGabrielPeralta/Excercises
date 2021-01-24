def main ():
    """
    El programa solicita al usuario que ingrese el nombre de una divisa para imprimirle su
    sibolo. Si la divisa  no  está en el diccionario se  le dará un aviso.
    """
    divisa = {'Euro':'€',       #Creamos un diccionario con las divisas
              'Dollar':'$',
              'Yen':'¥'}
    while True:                 #Iniciamos un ciclo while en true para que entre en el  cuerpo
        try:                    #Intentamos ejecutar las lineas de codigo siguientes, si no da error el break finaliza la operacion
            consultaDivisa = input("Ingrese la divisa y se mostrará su simbolo (Euro/Dollar/Yen): ")
            print (divisa[consultaDivisa])
            break
        except KeyError:        #Si arroja el error KeyError se imprime que la divisa no está y vuelve al try por el while.
            print("La divisa  no está en el diccionario")
    print("Programa finalizado")
main()
