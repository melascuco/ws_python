#! python3
# scriptJPGs.py

# pip install requests

import os, shutil
import logging
import requests, bs4

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')
print(' Script para descargar y renombrar los JPGs '.center(80,"~"));

print(os.getcwd())
print(os.listdir())
#os.chdir("sampledir")

# logging.debug('Downloading...')
# res = requests.get('https://www.adictosaltrabajo.com/wp-content/uploads/2017/02/1-1024x590.png')
# logging.debug('Downloaded!')

# res.raise_for_status()
# playFile = open('file.png', 'wb')
# for chunk in res.iter_content(100000):
	# playFile.write(chunk)
# playFile.close()

res = requests.get('http://www.fast-agile.com/method')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
type(noStarchSoup)

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