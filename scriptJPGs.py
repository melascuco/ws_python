#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install requests
# pip install beautifulsoup4

import os, shutil
import logging
import requests, bs4
import urllib.request

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

FOLDER_NAME = 'resultingJPGs'
URL_BASE = 'http://www.....ies_part_'
URL_BASE_B = '/CI20'
FILE_NAME_BASE = 's_s_c_'
PAGE_START = 1
PAGE_END = 1

logging.debug('Start of program')
print(' Script to download and rename imgs in consecutive urls '.center(80,"~"))

if not os.path.exists(FOLDER_NAME):
    logging.debug('Creating new folder')
    os.makedirs(FOLDER_NAME)
os.chdir(FOLDER_NAME)
print('Destination folder: ' + os.getcwd())

for urlIndex in range(PAGE_START, PAGE_END + 1):
    logging.info('Page: ' + str(urlIndex) + '... until ' + PAGE_END)
    currentPageA = URL_BASE + str(urlIndex)
    logging.debug('current page 1-20:' + currentPageA)
    currentPageB = URL_BASE + str(urlIndex) + URL_BASE_B
    logging.debug('current page 21-40:' + currentPageB)

    resA = requests.get(currentPageA)
    resA.raise_for_status()
    resASoup = bs4.BeautifulSoup(resA.text, "lxml")
    logging.debug('Current page A is loaded!')
    picsA = resASoup.select('div[class="photoset"] a img')
    indexForPics = 0
    for picA in picsA:
        indexForPics = indexForPics + 1
        urlToDownload = picA.get('src')
        logging.debug('To download: ' + urlToDownload)
        extension = urlToDownload[-4:]
        fileName = FILE_NAME_BASE + 'page' + str(urlIndex).rjust(4,'0') + '_pic' + str(indexForPics).rjust(2,'0') + extension
        logging.debug('File name: ' + fileName)
        urllib.request.urlretrieve (urlToDownload, fileName)

    resB = requests.get(currentPageA)
    resB.raise_for_status()
    resBSoup = bs4.BeautifulSoup(resB.text, "lxml")
    logging.debug('Current page B is loaded!')

    picsB = resBSoup.select('div[class="photoset"] a img')
    for picB in picsB:
        indexForPics = indexForPics + 1
        urlToDownload = picB.get('src')
        logging.debug('To download: ' + urlToDownload)
        extension = urlToDownload[-4:]
        fileName = FILE_NAME_BASE + 'page' + str(urlIndex).rjust(4,'0') + '_pic' + str(indexForPics).rjust(2,'0') + extension
        logging.debug('File name: ' + fileName)
        urllib.request.urlretrieve (urlToDownload, fileName)

print(' Fin '.center(80,"~"))
