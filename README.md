## Descripción General
### Breve introducción al proyecto:
"Este repositorio contiene un análisis y predicción de datos de negocios turísticos y de ocio usando datasets de Google y Yelp. Además, se implementan modelos de machine learning para predecir el éxito de un negocio, analizar sentimientos, predecir reseñas futuras y se incluye una muestra de datos con un despliegue en Streamlit."
Estructura del Proyecto
El proyecto está organizado en diferentes ramas que abordan análisis, limpieza de datos y machine learning:

### Rama Principal (main) Sergio Castro
Contiene el análisis y limpieza inicial del dataset Google.
Archivos clave:
ETL-google.ipynb : Limpieza del dataset Google y EDA.

### Rama Diana Moreno
Contiene el análisis y limpieza del dataset Yelp.
Archivos clave:
EDA-YELP.ipynb: EDA del dataset Yelp.
ETL-YELP.ipynb: Limpieza del dataset Yelp.

## Rama machine_learning Felipe Dedes
#### Descripción General
Esta rama se enfoca en el desarrollo del modelo de Machine Learning para predecir el éxito de negocios. Se incluyen análisis exploratorios, entrenamiento del modelo y visualizaciones de resultados en un mapa interactivo.

### Estructura de la Rama
#### .gitignore
Archivo que define los archivos y carpetas que no deben ser seguidos por Git.

#### EDA.ipynb
Notebook de Exploración de Datos (EDA):
Análisis inicial del dataset.
Limpieza y preparación de los datos para el modelo de Machine Learning.
#### Machine_Learning.ipynb
Notebook principal del desarrollo del modelo de Machine Learning:
Selección de variables y preparación del conjunto de datos.
Entrenamiento, evaluación y ajuste del modelo.
Métricas de rendimiento y resultados obtenidos.
#### business_success_map.html
Archivo HTML interactivo que visualiza las predicciones del modelo en formato de mapa.

#### README.md
Archivo de documentación que describe el contenido y uso de esta rama.

#### Objetivos de la Rama
Realizar un análisis exploratorio detallado de los datos.
Desarrollar y entrenar un modelo de Machine Learning para predecir el éxito de negocios.
Visualizar los resultados del modelo en un mapa interactivo

### Rama MLGretaCombold
Descripción General
Esta rama contiene un flujo completo de análisis, predicción y despliegue sobre una muestra de datos de Hawaii. Se enfoca en:

Exploración y limpieza de los datos.
Predicción del éxito de negocios con Machine Learning.
Despliegue interactivo mediante Streamlit.
Estructura de la Rama

Carpetas
info del deploy/
Contiene los recursos necesarios para el despliegue del modelo, análisis de datos y generación de visualizaciones.

Contenido de info del deploy/
Subcarpetas:

img/
Almacena imágenes y gráficos generados en el proceso de análisis o despliegue.
Archivos Clave:

Hawaii_predicciones.csv

Archivo con las predicciones finales realizadas sobre la muestra de datos de Hawaii.
Sintetica.csv

Muestra de datos sintéticos creada para pruebas y análisis.
analisis_sentimientos.py

Script en Python que realiza análisis de sentimientos en textos relacionados con los datos.
app.py

Script principal que despliega una aplicación interactiva utilizando Streamlit.
mapa.py

Genera un mapa de predicción visualizando el éxito de negocios según el modelo.
modelo_hawaii.pkl

Archivo serializado que contiene el modelo entrenado para realizar predicciones.
presentacion.py

Script para generar una presentación automática con los resultados del análisis.
requirements.txt

Lista de dependencias y librerías necesarias para ejecutar todos los scripts.

Archivos Principales en la Rama

**EDA.ipynb**
Notebook que realiza la Exploración de Datos (EDA) sobre la muestra de Hawaii.

**HawaiiMuestra.csv**
Archivo CSV original que contiene la muestra de datos de Hawaii.

**MuestraSintetica.ipynb**
Notebook donde se crea y analiza la muestra sintética para pruebas adicionales.

**PrediccionesHawaii.ipynb**
Notebook que aplica el modelo de Machine Learning para generar predicciones.

**READ.ME**
Archivo principal con la descripción del contenido de esta rama.

###Objetivo de la Rama
El propósito principal de esta rama es:

Realizar un análisis exploratorio y limpieza sobre datos de negocios de Hawaii.
Desarrollar un modelo de Machine Learning para predecir el éxito de un negocio.
Crear un despliegue interactivo de la solución usando Streamlit.
Proporcionar recursos adicionales como análisis de sentimientos y visualizaciones.


### Colaboradores:

Sergio Castro: Limpieza y análisis del dataset Google.
Diana Moreno: Limpieza y análisis del dataset Yelp.
Felipe Dedes : Machine learning y despliegue.
Greta Combold: Machine Learning y despliegue.
