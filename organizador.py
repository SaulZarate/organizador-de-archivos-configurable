import os
import shutil
import json

def getDataConfigJson( nameFile ):
    fileJson = open(nameFile)
    dataFile = fileJson.read()
    return json.loads(dataFile)

def checkAddress( address ):
    return  address if address[len(address)-1] == "/" else address + "/"


# CONSTANTES
DATA = getDataConfigJson( "config.json" )
FOLDER_ADDRESS = checkAddress( DATA["folderAddress"] )
FOLDERS = DATA["folders"]
OTHERS = DATA["others"]
NAME_FOLDER_OTHERS_FILES = "" if not OTHERS["inFolder"] else OTHERS["nameFolder"] 


""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~ FUNCIONES ~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """

def getContentFolder(srcFolder):
    if os.path.isdir(FOLDER_ADDRESS) :
        return os.listdir(FOLDER_ADDRESS)
    exit()

def getAddressFolder():
    return FOLDER_ADDRESS

def cleanArrayFiles(files):
    filesArray = []
    for i in files:
        if os.path.isfile(FOLDER_ADDRESS+i):
            filesArray.append(i)

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
        dicc[FOLDER_ADDRESS+fileName] = FOLDER_ADDRESS+getFolder(extension)
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
    pprint.pprint(filesAndFolders)
    for file,folder in filesAndFolders.items():
        # Creo la carpeta si es necesario
        createFolder(folder)
        # Muevo el archivo a la carpeta
        moveFile(file, folder)

def main():
    # Obtener la direccion de la carpeta actual
    srcFolder = getAddressFolder()

    # Contenido de la carpeta en array
    files = getContentFolder(srcFolder)
    
    # Solo guardo los archivos. Elimino las carpetas del array
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
main()
