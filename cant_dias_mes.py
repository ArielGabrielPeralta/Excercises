import es_biciesto                                  #Importamos la funcion "es_biciesto".

def cant_dias_mes (mes,anio):
    """
    Esta función segun los parametros "mes" y "anio" nos retornará la cantidad de dias que tendrá ese mes.
    """
    if mes in(1,3,7,8,10,12):                       #Si el mes es "1" ó "3" ó "7" ó "8" ó "10" ó "12".
        dias = 31                                       #Tendra un total de 31 dias.
    elif mes == 2:                                  #En el caso de que el mes sea "2".
        if es_biciesto.es_biciesto (anio):              #Si el año es biciesto.
            dias = 29                               #El mes 2 tendrá 29 dias.
        else:                                       #De lo contrario.
            dias = 28                                   #El mes 2 tendra 28 dias
    else:                                           #En caso contrario.
        dias = 30                                       #El mes tendrá 30 dias.
    return dias                                     #Retornamos dias.
