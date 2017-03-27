#! python3
# scriptJPGs.py

# pip install requests

import os, shutil
import logging
import requests

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')
print(' Script para descargar y renombrar los JPGs '.center(80,"~"));

os.path.join('C:\\jmario\\temp\\python\\sampledir')
print(os.getcwd())
print(os.listdir())
os.chdir("sampledir")
print(os.getcwd())


# Create results folder

# Takes a URL of a JPG and downloads it
# Asignar variables a cada parte de la url

# Bucle que abarque todas las páginas (según argumentos?)

# Descargar el html

# Abrir el html como string

# Buscar en el html el link a los 20 jpgs -> lista

# Borrar el html

# Recorrer la lista de 20 jpgs y descargar uno por uno

# Rename the JPG just downloaded
#shutil.move('fichero.txt', 'fichero_renombrado.txt')
# os.unlink('fichero_renombrado.txt')

print(' Fin '.center(80,"~"));