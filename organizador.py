import os
import shutil
import json
import pprint

def getDataConfigJson( nameFile ):
    fileJson = open(nameFile)
    dataFile = fileJson.read()
    return json.loads(dataFile)

DATA = getDataConfigJson( "config.json" )

# CONSTANTES
FOLDER_ADDRESS = DATA["folderAddress"]
FOLDERS = DATA["folders"]
OTHERS = DATA["others"]
NAME_FOLDER_OTHERS_FILES = "" if not OTHERS["inFolder"] else OTHERS["nameFolder"] 

pprint.pprint( os.listdir(FOLDER_ADDRESS) )

""" pprint.pprint( FOLDER_ADDRESS )
pprint.pprint( FOLDERS )
pprint.pprint( OTHERS ) """


""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~ FUNCIONES ~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """

def getAddressFolder():
    return os.getcwd()

def cleanArrayFiles(files):
    filesArray = []
    for i in files:
        if os.path.isfile(i):
            filesArray.append(i)
    
    # Obtener el nombre del archivo actual
    fileName = os.path.split(os.path.abspath(__file__))[1]
    # Otra forma de hacerlo => # fullPathName = __file__.split("\\")[-1] 

    # Eliminar el nombre del archivo actual
    filesArray.remove(fileName)
    # Elimino el archivo ejecutable
    fileNameExe = fileName[0:fileName.rfind(".")]+".exe"
    filesArray.remove(fileNameExe)
    # Elimino el archivo de configuracion
    filesArray.remove("config.json")

    return filesArray

def getExtension(filesName):
    indexExtension = filesName.rfind(".")
    extension = filesName[indexExtension:len(filesName)]
    return extension

def getFolder(extension):
    folder = NAME_FOLDER_OTHERS_FILES
    # Busca la carpeta
    for fol,ext in FOLDERS.items():
        if extension in ext:
            folder = fol

    return folder

def getFilesAndFolders(files):
    dicc = {}
    for fileName in files:
        extension = getExtension(fileName)
        dicc[fileName] = getFolder(extension)
    return dicc


def cleanDictionaryFiles( files ):
    newFiles = {}
    for file, folder in files.items():
        if folder != "":
            newFiles[file] = folder
    return newFiles

def createFolder(name):
    if not os.path.isdir(name):
        os.mkdir(name)

def moveFile(fileName, folderName):
    if os.path.isdir(folderName):
        shutil.move(fileName, folderName)

def createFoldersAndMoveFiles(filesAndFolders):
    for file,folder in filesAndFolders.items():
        # Creo la carpeta si es necesario
        createFolder(folder)
        # Muevo el archivo a la carpeta
        moveFile(file, folder)

def main():
    # Obtener la direccion de la carpeta actual
    srcFolder = getAddressFolder()

    # Contenido de la carpeta en array
    files = os.listdir(srcFolder)

    # Elimino el archivo .exe, .py, las carpetas y el archivo de configuracion .json
    files = cleanArrayFiles(files)

    if len(files) > 0:
        # Obtengo los archivos con sus carpetas correcpondientes y filtrados
        filesAndFolders = cleanDictionaryFiles( getFilesAndFolders(files) )

        # Creo las carpetas y muevo los archivos
        createFoldersAndMoveFiles(filesAndFolders)
    
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """


# Ejecuto el proyecto
#main()