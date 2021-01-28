def main ():
    """
    El programa solicita al usuario una lista de nombres, y otra de edades, estas
    son paralelas, por lo cual el indice 0 de una corresponde al  mismo  de la
    otra. Se  imprime en pantalla cada nombre con su edad.
    """
    nombres = [] #Definimos las dos listas
    edades = []
    nombre_solicitado = input("Ingrese el nombre de la persona (0 para terminar): ")
    if nombre_solicitado=="0":  #Solicitamos el nombre, si es "0" se imprime el mensaje
        print("Tus listas no tiene datos")
    else:                       #Si no es "0" tambien se le pide la edad
        edad_solicitada = int(input("Ingrese la edad de la persona: "))
    
    while nombre_solicitado!="0": #Mientras que el nombre sea distinto de "0"
            nombres.append(nombre_solicitado)   #apendamos a la lista lo solicitado
            edades.append(edad_solicitada)
        
            nombre_solicitado = input("Ingrese el nombre de la persona (0 para terminar): ")
            if nombre_solicitado=="0":  #Volvemos a solicitar  pero ahora si es  "0" se imprime los nombres y su edad correspondiente
                for i in range(len(nombres)):
                    print (nombres[i],"tiene ",edades [i])
            else:
                edad_solicitada = int(input("Ingrese la edad de la persona: "))

    #print(nombres,edades)
    print("El programa finalizó")

main()
