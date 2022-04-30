# Utilización de PSS/E con Python

---

## Objetivo

Con este repositorio se pretende documentar y explicar la forma en que se utiliza y funciona *PSS/E* a través de los comandos que existen para `Python`, con el objetivo de crear *Jupyter NoteBooks* para realizar análisis de flujos de potencia y otras actividades relevantes para el proceso de planeación.   

---

## Herrameintas quese utilizan

[Python](https://www.python.org/) 

Este lenguaje de programación es el principal componente de este repositorio y para entenderlo hay múltiples recursos graatuitos disponibles para su aprendizaje. En la *Wiki* de este repositorio se pondrán algunos recursos que pueden ser consultados y que han servido para los usuarios de este documento.

[IPython](https://ipython.readthedocs.io/en/stable/index.html) y [Jupyter](https://jupyter.org/) 

Interprete *interactivo* de _Python_ que se utiliza para la creación de *Note Books* con amplios propósitos. (En la wiki de este repositorio se colocaron algunas ligas con ejemplos de estos *Note Books* así como videos demostrativos para que te vayas familiarizando/interesando, sugiero los revises antes de continuar)  

[Visual Studio Code](https://code.visualstudio.com/) (recomendado) 

Editor de código con múltiples funcionalidades (extensiones) y en el cual se pueden ejecutar y desarrollar códigos de `Python` y `Jupyter NoteBooks`

## Primeros pasos

El uso de _Jupyter NoteBooks_ que se plantea es a través de *Visual Studio Code (VSC)* pero puede ser con algún otro visualizador (_Jupyter NoteBook, Jupyter Lab, Google Colab, etc_). Lo importante es adecuar nuestro ambiente de trabajo para poder importar correctamente las librerías que se utilizan.

### PSS/E

El primer elemento que debemos tener cubierto es la instalación de _PSS/E_ en nuestros equipos. Para ello considerar:

*Versión del PSS/E:* Actualmente se cuenta con las versiones de _PSS/E_ `32`, `34` y `35` (con sus diferentes actualizaciones cada una), en general no se debe tener problema al trabajar con alguna de ellas en particular, sin embargo, los códigos de este repositorio se ejecutaron para la versión `34.6.0.`

*Versión de Python:* Cuando se instala una versión de _PSS/E_, implicitamente también se descarga alguna versión de _Python_ por defecto, con la cual funcionan adecuadamente las librerías que permiten la comunicación entre _Python_ y _PSS/E_. 

Se ha visto que la versión `34` de _PSS/E_ instala y/o funciona correctamente con las verisones `2.7` y `3.4` de _Python_, ambas en 32 bits. Esto lo puedes revisar en el directorio de instalación de _PSS/E_ con los archivos de instalación y las referencias a estas versiones de _Python_ en los nombres de los archivos que ahí se encuentran.

*Librería de Python para PSS/E:* Al igual que la versión de _Python_ que se instala por defecto en tu equipo, también se descarga una librería exprofesa para la utilización de _PSS/E_ a través de _Python_. El nombre de esta librería es **PSSPYXX**, donde las "X" representan la versión de la librería. 

Por ejemplo, si se trabaja con _Python_ `2.7` habrá que utilizar (importar) la librería **PSSPY27**, o bien, si fuera el caso de la versión `3.4` de _Python_ se debe importar la librería **PSSPY34**. 

### Python y IPython

Una vez identificada la versión de _Python_ que se tiene instalada, (de acuerdo con la versión de _PSS/E_ que se encuentra en tu equipo), se debe instalar el paquete que permite la utilización de _Jupyter Note Books_. En la documentación de _IPython_ [(ver aquí)](https://ipython.readthedocs.io/en/stable/install/kernel_install.html) se menciona que las nuevas versiones de esta paquetería (6.0 en adelante) ya no soportan versiones inferiores a _Python 3.3_, por esta razón se debe instalar una versión compatible IPython, de la familia 5.X. Para hacer esto sigue los siguientes pasos:

1. En la línea de comandos dirígete a la carpeta donde se instala la versión de _Python_ con la que vas a trabajar (en nuestro caso es la 2.7) y ejecuta los comandos:

`python -m pip install ipykernel`
`python -m ipykernel install --user`

```

C:\Python27>python -m pip install ipykernel

C:\Python27>python -m ipykernel --user

```

*Nota:* Esto debe ser suficiente para que el _kernel_ que se emplea para la utilización de _Note Books_ en _VSC_. En pasos posteriores podría encontrarse un error al momento de ejecutar el _Note Book_, para resolverlo recomiendan en esta [página](https://github.com/microsoft/vscode-jupyter/wiki/Failure-to-start-kernel-due-to-failures-related-to-win32api-module) que se vuelva a instalalar `pywin32`. En esta otra [liga](https://github.com/jupyter/notebook/issues/4980) también se mencionan algunas soluciones de instalar y reinstalar`pywin32` para resolver este problema.

Instalar nuevamente `pywin32`:

```
C:\Python27>python -m pip install pywin32

```

Desinstalar e instalar nuevamente `pywin32`:

```
C:\Python27>python -m pip uninstall pywin32

C:\Python27>python -m pip install pywin32

```

2. Abrir _VSC_ (si no tienes el programa instalado lo puedes descargar [aquí](https://code.visualstudio.com/docs/?dv=win64user)) y crear un nuevo archivo de _Jupyter Note Book_ (extensión `.ipynb`). (si tienes dudas o eres nuevo en la utilización de _VSC_ recomiendo que consultes la wiki de este repositorio para que revises el material que se encuentra referente al uso de _VSC_)
