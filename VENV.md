# Utilización de ambientes virtuales con Python y VS Code

Es importante crear ambientes virtuales para el desarrollo de proyectos con _Python_ ya que nos permite tener un entorno controlado, con las librerías necesarias y las versiones correctas para que nuestras aplicaciones funcionen correctamente. De este modo podemos tener un programa que funcionan adecuadamente con ciertas librerías y en cierta versión de _Python_ y otro que requiere ya sea una librería adiciona, otra versión de _Python_ o bien una versión antes o después de cierta paquetería. 

Para evitar estar viendo y adaptando las paqueterías que tenemos instaladas y hacer los ajustes correspondientes para alguna aplicación en particular, se tienen los abientes virtuales. Estos nos permiten compartir un mismo intérprete de _Python_ y en el instalar las librerías y versiones que se requieran para correr algún programa, sin que esto interfiera con las configuraciones que tengamos en nuestro ambiente base.

En _conda_ ya se tiene esta funcionalidad de crear ambientes virtuales y se pueden hacer de manera muy sencilla desde la interfase de _conda Navigator_. Sin embargo, también es posible crear entornos virtuales sin la necesidad de recurrir a _conda_, a través de _VENV_ (_virtual environment_).

Para crear un ambiente de este tipo:

1. Posicionarse en la ruta del _kernell_ de _Python_ con el que se quiere crear el ambiente virtual, por ejemplo, si tenemos instaladas dos o más versiones de _Python_ en nuestra computadora nos deberemos posicionar en la que queremos que nuestro ambiente virtual trabaje:

```
...
drwxr-xr-x 1 uard6 197609          0 Dec  8  2020  MSOCache/
drwxr-xr-x 1 uard6 197609          0 Sep 21  2021  OneDriveTemp/
drwxr-xr-x 1 uard6 197609          0 Jun  5  2021  PerfLogs/
drwxr-xr-x 1 uard6 197609          0 Jun 29 08:32 'Program Files'/
drwxr-xr-x 1 uard6 197609          0 May 18 18:35 'Program Files (x86)'/
drwxr-xr-x 1 uard6 197609          0 Jun 29 12:14  ProgramData/
drwxr-xr-x 1 uard6 197609          0 Apr 30 11:53  Python27/
drwxr-xr-x 1 uard6 197609          0 May 10 12:28  Python37/
drwxr-xr-x 1 uard6 197609          0 Oct 27  2021  Recovery/
drwxr-xr-x 1 uard6 197609          0 Jul  7 12:13 'System Volume Information'/
drwxr-xr-x 1 uard6 197609          0 Jul  6 20:25  Users/
drwxr-xr-x 1 uard6 197609          0 Jul  7 22:19  Windows/
...
```
En este caso tenemos dos versiones de _Python_ instaladas (2.7 y 3.7). Si queremos que nuestro ambiente virtual utilice _Python_ 3.7 habría que posicionarse en esa ruta y ejecutar el siguiente comando:

```
c:\Python37>
c:\Python37>python -m venv c:\.venv\pss
```

Donde "c:/.venv/pss" es la ruta donde se quiere instalar el ambiente virtual y ".venv" es solo el nombre de la carpeta que comúnmente se crea para guardar ahí todos los ambientes virtuales, pero puede especificarse en cualquier otra dirección.

Con esto se habrán creado todos los archivos necesarios para que esta carpeta se pueda llamar por algún intérprete y funcione correctamente con la versión de _Python_ especificada (3.7 en este caso).

Finalmente, para **activar** este ambiente virtual e instalar las paqueterías que se requieran, se hace mediante el siguiente comando:

```
c:\.venv\pss\Scripts\activate.bat
```
Esto nos devolverá una indicación de que ya estamos en nuestro ambiente:

```
(pss) c:\.venv\pss\Scripts>
```

# Seleccionando este ambiente en VS Code

Consultar el procedimiento [aquí](https://code.visualstudio.com/docs/python/environments)

---

# Referencias

[venv Python.org](https://docs.python.org/es/3/library/venv.html)

[How to Set Up a Virtual Environment in Python – And Why It's Useful](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
