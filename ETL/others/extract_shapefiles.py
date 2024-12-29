## Funcion para extraer los SHAPEFILES que vienen en formato ZIP.

import os
import zipfile


directory = r'F:\DataScience\PF - DataNova\datasets\External Data\shapefile\TIGER'

for file in os.listdir(directory):
    zip_file_path = directory + "\\"  + file
    with zipfile.ZipFile(zip_file_path, 'r') as z:
        z.extractall(path=directory)