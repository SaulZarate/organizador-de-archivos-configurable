import os
import json
import shutil

# Return void
def createFolders(direction, dataJson):
    extensions = dataJson["extensions"]
    others = dataJson["others"]
    for folderToCreate in  extensions.keys():
        if not os.path.isdir(direction+"\\"+folderToCreate) :
            os.makedirs(direction+"\\"+folderToCreate, 777)

    # Creo la carpeta Otros si el usuario lo requiere
    if others["inFolder"] :
        if not os.path.isdir(direction+"\\"+others["nameFolder"]):
            os.makedirs(direction+"\\"+others["nameFolder"], 777)

# Return array
def getFiles(directionFolder):
    listDir = os.listdir(directionFolder)
    files = []
    for i in listDir:
        if os.path.isfile(directionFolder+"\\"+str(i)) :
            files.append(i)
    return files

# return dictionary
def getDataConfig():
    file = open('config.json')
    dataConfigJson = file.read()
    return json.loads(dataConfigJson)

# return String
def searchFolder(fileName, extensiones):
    others = getDataConfig()["others"]
    for key,value in extensiones.items():
        for extensionFile in value:
            if(fileName.find(extensionFile) >= 0):
                return key
    """ Si no encuentro su carpeta verifico que el usuario quiera guardarla en otra carpeta.
    Devuelvo el nombre de la carpeta o un string vacio """
    return other["nameFolder"] if other["inFolder"] else ""

# return void
def moveFiles(directionFolder, fileName, folderName):
    # Si la carpeta esta vacia no muevo el archivo
    if folderName == "":
        return

    fullNameFile = directionFolder+"\\"+fileName
    fullNameFolder = directionFolder+"\\"+folderName
    # Muevo el archivo
    shutil.move(fullNameFile, fullNameFolder)
