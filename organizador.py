import os
import shutil
import pprint

# Extensiones de archivos por carpeta
DATA = {
    "folders" : {
        "videos" : [
            ".wm",
            ".wmv",	
            ".rpm",
            ".mov",
            ".qt",
            ".qtl",	
            ".m1v",
            ".mp2v",
            ".mp4",
            ".mpa",
            ".mpe",
            ".mpeg",
            ".mpg",
            ".mpv2",
            ".ivf",	
            ".dvd",
            ".wob",	
            ".div", 
            ".divx",
            ".bik",
            ".smk",	
            ".avi",	
            ".asf",
            ".lsf",
            ".asx"
        ],
        "images" : [
            ".jpeg",
            ".jpg",
            ".gif",
            ".png",
            ".tiff",
            ".tif",
            ".pdf",
            ".eps",
            ".svg",
            ".nmp",
            ".psd",
            ".ai",
            ".raw"
        ],
        "audios" : [
            ".mp3",
            ".mid", 
            ".midi",
            ".wav",
            ".wma",
            ".cda",
            ".ogg",
            ".ogm",
            ".aac",
            ".ac3",
            ".flac",
            ".aym"
        ],
        "compacteds" : [
            ".rar",
            ".zip"
        ],
        "microsoft_Office" : [
            ".docx",
            ".docm",
            ".dotx",
            ".dotm",
            ".doc",
            ".dot",
            ".xls",
            ".xlsx",
            ".xlsm",
            ".ppt",
            ".pps",
            ".pptx",
            ".ppsx"
        ]
    },
    "others" : {
        "inFolder" : True,
        "nameFolder" : "otros"
    }
}

""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~ FUNCIONES ~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """

def cleanArrayFiles(files):
    filesArray = []
    for i in files:
        if os.path.isfile(i):
            filesArray.append(i)
    
    # Obtener el nombre del archivo actual
    fileName = os.path.split(os.path.abspath(__file__))[1]
    # Otra forma de hacerlo => # fullPathName = __file__.split("\\")[-1] 

    # Eliminar el nombre del archivo actual del array de archivos
    filesArray.remove(fileName)

    # Elimino el archivo ejecutable del array
    fileNameExe = fileName[0:fileName.rfind(".")]+".exe"
    if os.path.isfile(fileNameExe):
        filesArray.remove(fileNameExe)

    return filesArray

def getExtension(filesName):
    indexExtension = filesName.rfind(".")
    extension = filesName[indexExtension:len(filesName)]
    return extension

def getFolder(extension):
    folder = "otros"

    # Carpetas con sus extensiones
    folderAndExtensions = DATA["folders"]

    # Busca la carpeta
    for fol,ext in folderAndExtensions.items():
        if extension in ext:
            folder = fol

    return folder

def getFilesAndFolders(files):
    dicc = {}
    for fileName in files:
        extension = getExtension(fileName)
        dicc[fileName] = getFolder(extension)
    return dicc

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
    srcFolder = os.getcwd()

    # Obtener los archivos de la carpeta
    files = os.listdir(srcFolder)

    # Elimino el archivo exe y las carpetas ( filtro el array )
    files = cleanArrayFiles(files)

    if len(files) > 0:
        # Obtengo los archivos con sus carpetas correcpondientes
        filesAndFolders = getFilesAndFolders(files)

        # Creo las carpetas y muevo los archivos
        createFoldersAndMoveFiles(filesAndFolders)
    
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """
""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """

# Ejecuto el proyecto
main()