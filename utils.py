import os
import json
import shutil


def createFolders(direction, arrayFolders):
    for folderToCreate in arrayFolders:
        if not os.path.isdir(direction+"\\"+folderToCreate) :
            os.makedirs(direction+"\\"+folderToCreate, 777)
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
    folder = "otros"
    for key,value in extensiones.items():
        for extensionFile in value:
            if(fileName.find(extensionFile) >= 0):
                folder = key
    return folder

def moveFiles(directionFolder, fileName, folderName):
    fullFileName = directionFolder+"\\"+fileName
    fullFolderName = directionFolder+"\\"+folderName
    shutil.move(fullFileName, fullFolderName)