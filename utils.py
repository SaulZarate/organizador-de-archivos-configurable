import os
import json
import shutil


def createFolders(direction, dataJson):
    extensions = dataJson["extensions"]
    others = dataJson["others"]
    for folderToCreate in  extensions.keys():
        if not os.path.isdir(direction+"\\"+folderToCreate) :
            os.makedirs(direction+"\\"+folderToCreate, 777)

    # Creo la carpeta Otros si el usuario lo requiere
    if others["inFolder"] :
        if not os.path.isdir(direction+"\\otros"):
            os.makedirs(direction+"\\otros", 777)

def getFiles(directionFolder):
    listDir = os.listdir(directionFolder)
    files = []
    for i in listDir:
        if os.path.isfile(directionFolder+"\\"+str(i)) :
            files.append(i)
    return files

def getDataConfig():
    file = open('config.json')
    dataConfigJson = file.read()
    return json.loads(dataConfigJson)

def searchFolder(fileName, extensiones):
    for key,value in extensiones.items():
        for extensionFile in value:
            if(fileName.find(extensionFile) >= 0):
                return key
    """ Si no encuentro su carpeta verifico que el usuario quiera guardarla en otra carpeta.
    Devuelvo el nombre de la carpeta o False """
    return getDataConfig()["others"]["nameFolder"] if getDataConfig()["others"]["inFolder"] else False

def moveFiles(directionFolder, fileName, folderName):
    # Si es False no se mueve el archivo
    if not folderName:
        return

    fullFileName = directionFolder+"\\"+fileName
    fullFolderName = directionFolder+"\\"+folderName
    # Muevo el archivo
    shutil.move(fullFileName, fullFolderName)
