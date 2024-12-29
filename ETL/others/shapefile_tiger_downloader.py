### Para determinar con precisión el estado y ciudad en base a coordenadas, usaremos archivos SHAPEFILES provistos por el gobierno de estados unidos.
#Este script se correrá para bajar el shapefile de los 51 estados de usa
import os
import requests

# Crear una lista de códigos de los 50 estados y territorios
state_codes = [
    "01", "02", "04", "05", "06", "08", "09", "10", "11", "12", "13", "15", "16", 
    "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", 
    "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", 
    "44", "45", "46", "47", "48", "49", "50", "51", "53", "54", "55", "56"
]

# Base URL para descargar shapefiles de Places
base_url = "https://www2.census.gov/geo/tiger/TIGER2024/PLACE/tl_2024_{state}_place.zip"

# Carpeta para guardar los archivos
output_dir = r"F:\DataScience\PF - DataNova\datasets\External Data\shapefile\TIGER"
os.makedirs(output_dir, exist_ok=True)

# Función para descargar y guardar shapefiles
def download_shapefiles():
    for state_code in state_codes:
        url = base_url.format(state=state_code)
        output_path = os.path.join(output_dir, f"tl_2024_{state_code}_place.zip")
        
        print(f"Descargando {url} ...")
        
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Verificar errores en la descarga
            
            # Guardar el archivo descargado
            with open(output_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            
            print(f"Archivo guardado en {output_path}")
        
        except requests.RequestException as e:
            print(f"Error descargando {url}: {e}")

# Ejecutar la función de descarga
download_shapefiles()