# Organizador de archivos configurable

_El proyecto se encarga de separar los archivos de una carpeta y moverlos a su carpeta correspondiente (creada con anterioridad). Tambien tiene la opcion de elegir que hacer con los archivos que no forman parte de ningun grupo, como por ejemplo decidir si se van a guardar en una carpeta llamada "otros" (por defecto) o simplemente no moverlos._

## Pre-requisitos 馃搵

```
Tener Window como sistema operativo
```

## Comenzando 馃殌

_Para utilizar este proyecto tiene que descargar este repositorio, configurar el archivo **config.json** y finalmente ejecutar el archivo organizador.exe_

_**Importante: Los archivos de config.json y organizador.exe deben permanecer en la misma carpeta**_

## Instalaci贸n/Descarga del proyecto 馃敡

_El proyecto no necesita instalaci贸n. Lo unico que necesita es descargar este repositorio. A continuaci贸n le indicare dos formas para realizarlo._

### Primera forma - Clonar el repositorio

* Instalar git
* Abrir git bash o la terminal que prefiera donde desee tener el proyecto
* Luego ingrese el siguiente comando
```
git clone https://github.com/SaulZarate/Python-organizadorDeArchivos.git
```
* Presione Enter y espere a que se descargue.


### Segunda forma - Descargar un .ZIP
* Dirijase a la parte superior de la p谩gina y presione click en el boton verde que dice Code
* Luego presione Download ZIP
* Dirijase a la carpeta donde se descargo el archivo .ZIP y luego descomprima el archivo

## Despliegue 馃摝
* Copie la direccion de la carpeta que desee organizar (puede usar rutas absolutas o relativas)
* Abra el archivo **config.json** con cualquier programa ( por ejemplo con un blog de notas )
* Pegue la direccion de la carpeta donde estan los tres puntos.
``` 
Ejemplo: "C:/Users/nombreDeUsuario/Escritorio"
```
* **隆隆隆 Cuidado: !!!** Si vas a ingresar una ruta con las barras del tipo "\\". Debe ingresar dos por cada barra. Ejemplo a continuaci贸n:
```
Direcci贸n original: "C:\Users\nombreDeUsuario\Escritorio"

Direcci贸n a ingresar: "C:\\Users\\nombreDeUsuario\\Escritorio" 
```

## Configuraciones 鈿欙笍
_En el archivo **config.json** puede cambiar las configuraciones por defecto y agregar nuevas carpetas/grupos._
### Archivos sin carpeta/grupo
* inFolder  => Indica si queremos guardar los archivos sin carpeta/grupo en una carpeta.
    - true = Guardar en una carpeta
    - false = No guardarlos en una carpeta
* nameFolder => Es el nombre de la carpeta donde se van a guardar los archivos que no tienen carpeta/grupo.
```
"others" : {
        "inFolder" : true,
        "nameFolder" : "otros"
    }
```
### Agregar carpetas/grupos
* Estructura por defecto
```
"folders" : {
        "videos" : [...],
        "images" : [...],
        "audios" : [...],
        "compacteds" : [...],
        "microsoft_Office" : [...]
}
```
* Agregar una carpeta/grupo. Ejemplo:
```
"folders" : {
        "videos" : [...],
        "images" : [...],
        "audios" : [...],
        "compacteds" : [...],
        "microsoft_Office" : [...],
        "Lenguajes_de_programacion" : [".py",".js",".java","etc..."]
}
```
* **Importante:** Observer que he agregado una coma "," al final de la ultima linea original => "microsoft_Office" : [...] **,** 
    * Si no agrega la coma, el ejecutable no va a funcionar.
    * Si solo desea agregar una extension, tambien debe ingresarlo entre corchetes (en el array). **[".py"]**
    * Antes de agregar una extension no olvide revisar en las otras carpetas/grupos si ya la tienen. En cuyo caso, borrelas.

## Construido con 馃洜锔?

* [Python](https://docs.python.org/) - Lenguaje de programaci贸n
* [pip](https://pip.pypa.io/en/stable/installing/) - Manejador de dependencias
* [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html) - Usado para convertir archivos .py a un ejecutable

## Autor 鉁掞笍

* **Saul Zarate** - *Desarrollador*
