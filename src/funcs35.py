import psse35
import psspy
import redirect
import math
import pandas as pd

def dic_flujos(ssid=0,volt=[0,400],gcr=[3,5,6]):
    '''
        Función que crea un diccionario de líneas y transformadores de 2 devanados, cuya clave es: 
        #BUSFROM-#BUSTO-ID y sus valores son: P, Q, MVA y PLOSS (en ese orden)
        El diccionario se crea con los elementos que resulten del subsistema que se especifiquen en los argumentos. Solo considera filtros de:
        Vmin, Vmax y Gerencia de Control
        Args:
            ssid (int): Número del subsistema que se va a crear
            volt (list): Lista de dos elementos, el primero es el Vmin y el segundo corresponde a Vmax
            gcr (list): Lista de las Gerencias que se desan
        Returns:
            flujos_dict (dict): Diccionario con la siguiente forma: 
            {#BUSFROM-#BUSTO-ID: (P,Q,MVA,PLOSS) -para LT y TR 2WND
             #BUSFROM-ID:(P,Q,MAXMVA) -para TR 3WND}
    '''
    ierr = psspy.bsys(ssid,1,volt,len(gcr),gcr,0,[],0,[],0,[]) 
    ierr, ids = psspy.aflowchar(0,1,6,2, string=["ID"])
    ierr, numeros = psspy.aflowint(0,1,6,2, string=["FROMNUMBER","TONUMBER"])
    ierr, flujo = psspy.aflowreal(0,1,6,2, string=["P","Q","MVA","PLOSS"])
    
    #Crea claves de enlaces [#FROM_BUS - #TO_BUS - ID, #FROM_BUS - #TO_BUS - ID, ... ] -Para identificar transformadores de 3 devanados
    ramas_list = []
    for elem in range(len(ids[0])):
        ramas_list.append(str(numeros[0][elem]) + '-' + str(numeros[1][elem]) + '-' + str(ids[0][elem]).strip())

    #Crea diccionario, donde la llave es la clave del enlace y sus valores son los flujos de potencia por el elemento (LT o TR 2WND):
    valores = list(zip(*flujo))
    flujos_dict = {}
    for i in range(len(flujo[0])):
        flujos_dict[ramas_list[i]] = valores[i]
    
    # Obtiene flujo de los transformadores de 3 devanados de las Gerencias especificadas
    ierr = psspy.bsys(1,1,[69,400],len(gcr),gcr,0,[],0,[],0,[]) 
    ierr, ides = psspy.awndchar(1, 1, 3, 1, 1, string=['ID'])
    ierr, wndbus = psspy.awndint(1, 1, 3, 1, 1, string=['WNDBUSNUMBER'])
    ierr, wndflw = psspy.awndreal(1, 1, 3, 1, 1, string=['P','Q','MAXMVA'])

    #Crea claves de enlaces [#FROM_BUS - ID, #FROM_BUS - ID, ... ] -Para identificar transformadores de 3 devanados
    tr_list = []
    for elem in range(len(ides[0])):
        tr_list.append(str(wndbus[0][elem]) + '-' + str(ides[0][elem]).strip())
    
    #Adiciona al diccionario los flujos de potencia por el elemento de TR 3WND:
    valores_tr = list(zip(*wndflw))
    for i in range(len(wndflw[0])):
        flujos_dict[tr_list[i]] = valores_tr[i]
    
    return flujos_dict
