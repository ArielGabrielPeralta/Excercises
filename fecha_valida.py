import  cant_dias_mes                                                                           #Importamos la funcion "cant_dias_mes".

def fecha_valida (dia, mes, anio):
    """
    La función nos permitirá validar la fecha con los parametros "dia", "mes" y "anio".
    """
    valida = False                                                                              #Definimos la variable "valida" y le asignamos el valor "False"
    if dia >=1 and mes >=1 and mes <=12 and dia <= cant_dias_mes.cant_dias_mes (mes,anio):      #Si dia es mayor o igual a 1 y mes es mayor o igual a 1 y mes es menor o igual a 12 y dia es menor o igual a los parametros que devuelve "cant_dias_mes".
        valida = True                                                                           #La variable "valida" será "True".
    else:                                                                                       #Sino.
        valida = False                                                                          #La variable "valida" será "False"
    
    return valida                                                                               #Retormanos "valida".
