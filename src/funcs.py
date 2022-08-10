import psse34
import psspy
import redirect
import math
import pandas as pd

def carga_area(areas):
    '''
        Obtiene la carga de una o varias areas del sistema.
        Args:
            areas (list): Listado de las areas que se quieren consultar,
        Returns:
            MW (list): Lista con los valores de la potencia activa en cada area. 
            MVAr (list): Lista con los valores de la potencia reactiva en cada area.
            MVA (list): Lista con los valores de la potencia aparente en cada area.
            FP (list): Lista con los valores del factor de potencia en cada area.
    '''
    # Establecer los arreglos en donde se almacenaran los resultados
    MW = []
    MVAr = []
    MVA = []
    FP = []
    # Crear el ciclo y el orden en que se ejecutaran las tareas
    for area in areas:
        psspy.asys(0, 1, [area])
        ierr, xarray = psspy.aareacplx(0, 1, ['PQLOAD'])
        MW.append(xarray[0][0].real)
        MVAr.append(xarray[0][0].imag)
        MVA.append(abs(xarray[0][0]))
        FP.append(xarray[0][0].real/abs(xarray[0][0]))
    return areas, MW , MVAr, MVA, FP

def crea_df(nom_cols,val_cols):
    '''
        Crea un DataFrame con los nombres de columna y los valores de cada columna.
        Args:
            nom_cols (list): Listado de las nombres de columna que se desean en el Data Frame
            val_cols (tuple): Tupla con los valores de las variables referentes a cada columna de nom_cols (cada elemento de la lista es tambien una lista)
        Returns:
            df (DataFrame): Data Frame con los elementos proporcionados 
    '''
    it = 0
    df = pd.DataFrame()
    for nom in nom_cols:
        df[nom] = val_cols[it]
        it += 1
    return df

#def casos_dir(path=CASOS_PATH):
#    casos_sav = os.listdir(path)
#    return casos_sav