import fecha_valida

def fecha_siguiente (dia,mes,anio):
    """
    Esta funcion se utilizará para retornar la fecha siguiente de un dia, mes y anio
    especifico, dado por paramertos
    """

    if not fecha_valida.fecha_valida (dia,mes,anio): #si la fecha no es valida se devolverá el -1 en cada prametro
        dia_sig = -1
        mes_sig = -1
        anio_sig = -1
    elif fecha_valida.fecha_valida (dia+1,mes,anio): #si al sumar 1 al dia la fecha es valida se devolverá la fecha siguiente
        dia_sig = dia+1
        mes_sig = mes
        anio_sig = anio
    elif fecha_valida.fecha_valida (dia,mes+1,anio): #si es cambio de mes se sumará uno al mes y el dia será 1
        dia_sig = 1
        mes_sig = mes+1
        anio_sig = anio
    else :                              #si es cambio de año el dia y el mes serán 1 y se sumará 1 al año
        dia_sig = 1
        mes_sig = 1
        anio_sig = anio+1

    return dia_sig, mes_sig, anio_sig #se retorna el dia mes y año correspondiente
