import os
import sys

#Damos de alta los directorios de psse,para correrlo sin abrirlo

PSSPY_location = r'C:\Program Files\PTI\PSSE35\35.0\PSSPY37' #hay que cambiar la ruta dependianto si se usa psse34 o 35 tambien en base al python 2 o 3
PSSE_location = r'C:\Program Files\PTI\PSSE35\35.0\PSSBIN' #hay que cambiar la ruta dependianto si se usa psse34 o 35
sys.path.append(PSSPY_location)
sys.path.append(PSSE_location)
os.environ['PATH'] += ';' + PSSPY_location
os.environ['PATH'] += ';' + PSSE_location

#Importamos librerias del PSS

import psse35
import psspy
import redirect

redirect.psse2py()

psspy.psseinit(50000)