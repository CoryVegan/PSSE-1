'''
Funciones que realizan pruebas en los casos de PSS/E que se tengan abiertos para verificar que estén modelados los PEMs instruidos.
'''

import psspy

def dictbus():
  '''
  Función que crea un diccionario con la siguiente estructura:

  {#BUS1 : NOMBRE, #BUS2 : NOMBRE, ...}
  
  '''
  ierr, carray = psspy.abuschar(0, 1, 'NAME')
  ierr, iarray = psspy.abusint(0, 1, 'NUMBER')
  buses_dict = {}
  for i in range(len(iarray[0])):
    buses_dict[iarray[0][i]] = carray[0][i]
  return buses_dict

def lista_enlaces():
  '''
  Función que crea una lista con las claves de los enlaces (LT y 2WND-TR):

  [#FROM_BUS - ID - #TO_BUS, #FROM_BUS - ID - #TO_BUS, ... ]
  
  '''
  ierr, ids = psspy.abrnchar(0,1,3,4,2, string=["ID"])
  ierr, numeros = psspy.abrnint(0,1,3,4,2, string=["FROMNUMBER","TONUMBER"])
  ramas_list = []
  for elem in range(len(ids[0])):
    ramas_list.append(str(numeros[0][elem]) + '-' + str(ids[0][elem]) + '-' + str(numeros[1][elem]))
  return ramas_list

# ----------------- Funciones para verificar cada PEM ---------------------------------

def P16_OC2():
    '''
    Obras: 
           TR 400/115 en Potrerillos + 
           Traslado de TR 230/115 kV de Potrerillos a León III +
           LT 115 kV Potrerillos - San Roque +
           LT 115 kV Potrerillos entronque León I - Ayala

    Verificación: 
                  Existen los Buses:
                    330704:'POS-13.8T4' 
                    330803:'LNT-13.8T3'
                  Existen los circuitos: 
                    (POS-115)33045-OC-33019(SRQ-115)
                    (POS-115)33045-OC-33032(LNU-115)
                    (POS-115)33045-OC-33036(AYA-115)
                  No existe el circuito:
                    (LNU-115)33032-73-33036(AYA-115)
    '''
    # Verificación de Buses

    BUSES = {330704:'POS-13.8T4',330803:'LNT-13.8T3'}
    
    buses_dict = dictbus()

    for clave, valor in BUSES.items():
        try:
            if buses_dict[clave].strip() != valor:
              return print('Hay un problema con el Bus: ', clave)
        except:
            print('El Bus:', clave, 'no existe')
        else:
            print('Bus:', clave, 'ok')

    # Verificación de Enlaces

    ENLACES_IN = ['33045-OC-33019',
                  '33045-OC-33032',
                  '33045-OC-33036']
    
    ENLACES_OUT = ['33032-73-33036']
    
    ramas_list = lista_enlaces()

    for clave in ENLACES_IN:
        if clave not in ramas_list:
          return print('Hay un problema con el enlace: ', clave)
        else:
            print('Enlace:', clave, 'ok')

    for clave in ENLACES_OUT:
        if clave in ramas_list:
          return print('Hay un problema con el enlace: ', clave)
        else:
            print('Enlace:', clave, 'ok')      

  
