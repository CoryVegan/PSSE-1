'''
Funciones que realizan pruebas en los casos de PSS/E que se tengan abiertos para verificar que estén modelados los PEMs instruidos.
'''

import psspy

def comp_bus(BUSES):
  '''
  Función que crea un diccionario con la siguiente estructura:

  {#BUS1 : NOMBRE, #BUS2 : NOMBRE, ...}
  
  Y busca en ese diccionario los buses que se le pidan en la variable BUSES, la cual debe ser un diccionario también con la misma estructura. 
  '''
  ierr, carray = psspy.abuschar(0, 1, 'NAME')
  ierr, iarray = psspy.abusint(0, 1, 'NUMBER')
  buses_dict = {}
  for i in range(len(iarray[0])):
    buses_dict[iarray[0][i]] = carray[0][i]

  for clave, valor in BUSES.items():
        try:
            if buses_dict[clave].strip() != valor:
              return print('Hay un problema con el Bus: ', clave)
        except:
          print('El Bus:', clave, 'no existe')
        else:
          return print('Bus:', clave, 'ok')

def comp_shunt(SHUNTS_IN):
  '''
  Función que crea un diccionario con la siguiente estructura:

  {#BUS1/BUSNAME1(ID) : SHUNTMVAr, #BUS2/BUSNAME2(ID) : SHUNTMVAr, ...}
  
  Y busca en ese diccionario los buses que se le pidan en la variable SHUNTS, la cual debe ser un diccionario también con la misma estructura. 
  '''
  ierr, iarray = psspy.afxshuntint(0, 4, string=['NUMBER'])
  ierr, carray = psspy.afxshuntchar(0, 4, string=['NAME','ID'])
  ierr, xarray = psspy.afxshuntreal(0, 4, string=['SHUNTNOM'])
  shunt_dict = {}
  for elem in range(len(iarray[0])):
    shunt_dict[str(iarray[0][elem]) + '/' + carray[0][elem].strip() + '(' + carray[1][elem] + ')'] = xarray[0][elem]

  for clave, valor in SHUNTS_IN.items():
        try:
            if abs(shunt_dict[clave] - valor) > 1:
              return print('Hay un problema con el Shunt: ', clave)
        except:
             print('El Shunt:', clave, 'no existe')
        else:
            print('Shunt:', clave, 'ok')

def comp_enlaces(ENLACES_IN = 0, ENLACES_OUT = 0):
  '''
  Función que crea una lista con las claves de los enlaces (LT y 2WND-TR):

  [#FROM_BUS - ID - #TO_BUS, #FROM_BUS - ID - #TO_BUS, ... ]
  
  La función hace dos búsquedas:
  1. Que se encuentren los enlaces de la variable ENLACES_IN, la cual debe ser una lista también con la misma estructura.
  2. Que no existan los enlaces de la variable ENLACES_OUT, la cual debe ser una lista también con la misma estructura.

  En caso de no haber enlaces "in" o "out" para verificar, se pone un cero '0' en la posición que corresponda. 
  
  '''
  ierr, ids = psspy.abrnchar(0,1,3,4,2, string=["ID"])
  ierr, numeros = psspy.abrnint(0,1,3,4,2, string=["FROMNUMBER","TONUMBER"])
  
  ramas_list = []
  for elem in range(len(ids[0])):
    ramas_list.append(str(numeros[0][elem]) + '-' + str(ids[0][elem]) + '-' + str(numeros[1][elem]))
  
  try:
    for clave in ENLACES_IN:
      if clave not in ramas_list:
        return print('Hay un problema con el enlace: ', clave)
      else:
        print('Enlace:', clave, 'ok')
  except:
    print('Lista de ENLACES_IN vacía o con error:',ENLACES_IN)
  
  try:
    for clave in ENLACES_OUT:
        if clave in ramas_list:
          return print('Hay un problema con el enlace: ', clave)
        else:
            print('Enlace:', clave, 'ok')
  except:
    print('Lista de ENLACES_OUT vacía o con error:',ENLACES_OUT)

# ----------------- Funciones para verificar cada PEM ---------------------------------

def P16_OC2():
    '''
    Potrerillos Banco 4
    
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
    print('PEM P16-OC2')

    # Verificación de Buses
    BUSES = {330704:'POS-13.8T4',330803:'LNT-13.8T3'}
    comp_bus(BUSES)

    # Verificación de Enlaces
    ENLACES_IN = ['33045-OC-33019',
                  '33045-OC-33032',
                  '33045-OC-33036']

    ENLACES_OUT = ['33032-73-33036']
    comp_enlaces(ENLACES_IN,ENLACES_OUT)

    print('-----------------------------')

    return

def P18_OC9():
    '''
    Compensación capacitiva de la Zona Querétaro
    (obras con cambio de alcance)
    
    Obras: 
           CAP 15.0 en Parque Innovación (antes en Aeroespacial 22.5 MVAr) + 
           CAP 30.0 en Querétaro Potencia (antes en Campanario 15 MVAr) +
           CAP 22.5 en Conín (antes en San Ildefonso 30 MVAr) +
           CAP 22.5 en Antea (antes en Montenegro 22.5 MVAr) +
           CAP 30.0 en Cimatario +
           CAP 15.0 en Querétaro I
           
     Verificación: 
                  Existen los capacitores:
                    34043/PQN-115(OC): 15.0
                    34116/QRP-115(OC): 30.0
                    34140/CNI-115(OC): 22.5
                    34114/NTA-115(OC): 22.5
                    34160/CIM-115(OC): 30.0
                    34112/QRO-115(OC): 15.0
    '''
    print('PEM P18-OC9')  
       
    SHUNTS_IN = {'34043/PQN-115(OC)': 15.0,
                 '34116/QRP-115(OC)': 30.0,
                 '34140/CNI-115(OC)': 22.5,
                 '34114/NTA-115(OC)': 22.5,
                 '34160/CIM-115(OC)': 30.0,
                 '34112/QRO-115(OC)': 15.0}

    comp_shunt(SHUNTS_IN)

    print('-----------------------------')

    return

def P19_NT1():
    '''
    Terranova Banco 2
    
    Obras: 
           TR 230/115 en Terranova
           
    Verificación: 
                  Existe el Bus:
                    55850:'TER-Y2' 
    '''
    print('PEM P19-NT1')

    # Verificación de Buses
    BUSES = {55850:'TER-Y2'}
    comp_bus(BUSES)

    print('-----------------------------')

    return

def P17_NT2():
    '''
    Nuevo Casas Grandes Banco 3
    
    Obras: 
           TR 230/115 en Nuevo Casas Grandes
           CAP 30.0 en Nuevo Casas Grandes
           
    Verificación: 
                  Existe el Bus:
                    55901:'NCG-Y3' 
    '''
    print('PEM P17-NT2')

    # Verificación de Buses
    BUSES = {55901:'NCG-Y3'}
    comp_bus(BUSES)

    # Verificación de Shunts
    SHUNTS_IN = {'5536/NCG-115(NT)': 30.0}

    comp_shunt(SHUNTS_IN)

    print('-----------------------------')

    return

def P15_NT1():
    '''
    Chihuahua Norte Banco 5
    
    Obras: 
           TR 230/115 en Chihuahua Norte (sustitución de dos de 100 por uno de 300 MVA) + 
           TR 230/115 en Ávalos (traslado de uno de los bancos de 100 MVA)
           
    Verificación: 
                  Existen Buses:
                    549970:'CUN-Y5'
                      5469:'AVL-Y3' 
    '''
    print('PEM P15-NT1')

    # Verificación de Buses
    BUSES = {549970:'CUN-Y5',
             5469:'AVL-Y3'}
    comp_bus(BUSES)

    print('-----------------------------')

    return

def P16_NT1():
    '''
    Zona La Laguna
    
    Obras: 
           TR 400/115 en Torreón Sur
           LT Torreón Oriente - California (OBRA CON PROBLEMÁTICAS DE CONSTRUCCIÓN)
           **LT Torreón Oriente - Abastos (NO INCLUIDA EN PROYECTO ORIGINAL)
           **LT Torreón Sur entronque Revolución - Allende (NO INCLUIDA EN PROYECTO ORIGINAL)
           Recalibraciones:
            Takata - Torreón Sur
            Takata - Torreón Oriente
            Torreón Sur - Maniobras Mieleras
            Maniobras Mieleras - Diagonal
            Torreón Sur - Torreón Oriente
           
    Verificación: 
                  Existen Buses:
                    51854:'TRS-Y5'
                  Existen los circuitos:
                    (TOT-115)5058-NT-5031(CFN-115)
                    (TAK-115)5090-NT-5060(TRS-115)
                    (TAK-115)5090-NT-5058(TOT-115)
                    (TRS-115)5060-NT-5039(MMI-115)
                    (DGN-115)5068-NT-5039(MMI-115)
                    (TOT-115)5058-NT-5060(TRS-115)
    '''
    print('PEM P16-NT1')

    # Verificación de Buses
    BUSES = {51854:'TRS-Y5'}
    comp_bus(BUSES)

    # Verificación de Enlaces
    ENLACES_IN = ['5058-NT-5031',
                  '5090-NT-5060',
                  '5090-NT-5058',
                  '5060-NT-5039',
                  '5068-NT-5039',
                  '5058-NT-5060']

    comp_enlaces(ENLACES_IN,0)

    print('-----------------------------')

    return