import psse35
import psspy
import redirect
import math
import pandas as pd

def dic_flujos():
 
    ierr, ids = psspy.aflowchar(0,1,6,2, string=["ID"])
    ierr, numeros = psspy.aflowint(0,1,6,2, string=["FROMNUMBER","TONUMBER"])
    ierr, flujo = psspy.aflowreal(0,1,6,2, string=["P","Q","MVA","PLOSS"])
    #Crea claves de enlaces [#FROM_BUS - ID - #TO_BUS, #FROM_BUS - ID - #TO_BUS, ... ]
    ramas_list = []

    for elem in range(len(ids[0])):
        ramas_list.append(str(numeros[0][elem]) + '-' + str(numeros[1][elem]) + '-' + str(ids[0][elem]).strip())

    valores = list(zip(*flujo))

    #Crea diccionario, donde la llave es la clave del enlace y sus valores son los flujos de potencia por el elemento:
    flujos_dict = {}
    for i in range(len(flujo[0])):
        flujos_dict[ramas_list[i]] = valores[i]
    return flujos_dict
