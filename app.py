
# Importo mis funciones
import utils

""" Obtenemos los datos necesarios del archivo Json """
data = utils.getDataConfig()

# Carpetas y sus extensiones
extensions = data["extensions"]

# Direccion de la carpeta a organizar
directionFolder = data["folderToOrganize"]

# contenido de la carpeta en array
files = utils.getFiles(directionFolder)

# Verifico que la carpeta tenga archivos 
if len(files) > 0:

    # Si no existen las carpetas las creo
    utils.createFolders(directionFolder, data)

    # Mover archivos a sus carpetas correspondientes
    for fileName in files:
        # Carpeta a la que pertenece cada archivo
        folder = utils.searchFolder(fileName, extensions)
        
        # Muevo los archivos a sus carpetas
        utils.moveFiles(directionFolder, fileName, folder)

