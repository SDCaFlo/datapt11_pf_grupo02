## Descripción General

### Breve introducción al proyecto:
"Este repositorio contiene un análisis y predicción de datos de negocios turísticos y de ocio usando datasets de Google y Yelp. Además, se implementan modelos de machine learning para predecir el éxito de un negocio, analizar sentimientos, predecir reseñas futuras y se incluye una muestra de datos con un despliegue en Streamlit."
Estructura del Proyecto
El proyecto está organizado en diferentes ramas que abordan análisis, limpieza de datos y machine learning:

## Rama Principal (main) Sergio Castro
Descripción General
La rama principal contiene el proceso de ETL y la culminación del Análisis Exploratorio de Datos (EDA) del dataset Google. Esta rama sirve como base principal del proyecto, consolidando el trabajo inicial sobre los datos.

### Estructura de la Rama
#### ETL-google.ipynb

Notebook que realiza el proceso ETL (Extracción, Transformación y Carga) del dataset Google.
Contenido:
Extracción de datos crudos.
Transformación: limpieza, eliminación de valores nulos y duplicados.
Preparación de los datos para su posterior análisis y modelado.
Resultados finales del EDA, donde se exploran tendencias y características clave de los datos.
#### README.md

Archivo de documentación que describe la estructura y propósito del proyecto

#### Objetivos de la Rama Sergio Castro 
Realizar la preparación de datos con un proceso ETL sobre el dataset Google.
Culminar el Análisis Exploratorio de Datos (EDA) para comprender las tendencias y características principales del dataset.
Consolidar la base de datos lista para los siguientes análisis y modelado.

## Rama Diana Moreno
### Descripción General
Esta rama contiene el análisis exploratorio de datos (EDA) y el proceso de Extracción, Transformación y Carga (ETL) del dataset Yelp. El objetivo es preparar y analizar los datos para su uso posterior en el proyecto.

### Estructura de la Rama
#### EDA-YELP.ipynb

Notebook que realiza la Exploración de Datos (EDA) del dataset Yelp.
Contenido:
Análisis inicial de las características de los datos.
Identificación de valores nulos, duplicados y distribuciones.
Visualización de patrones y tendencias.

#### ETL-YELP.ipynb

Notebook que implementa el proceso de Extracción, Transformación y Carga (ETL) de los datos de Yelp.
Contenido:
Extracción de datos crudos.
Transformación: limpieza, eliminación de inconsistencias y creación de nuevas variables.
Preparación de los datos para análisis o modelado.
Objetivos de la Rama
Realizar un análisis exploratorio para entender la estructura y calidad del dataset Yelp.
Implementar un proceso de ETL para preparar los datos para futuros análisis y modelado.

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

## Rama MLGretaCombold
#### Descripción General
Esta rama contiene un flujo completo de análisis, predicción y despliegue sobre una muestra de datos de Hawaii. Se enfoca en:
Exploración y limpieza de los datos.
Predicción del éxito de negocios con Machine Learning.
Despliegue interactivo mediante Streamlit.
Estructura de la Rama

#### Carpetas
info del deploy/
Contiene los recursos necesarios para el despliegue del modelo, análisis de datos y generación de visualizaciones.

Contenido de info del deploy/
Subcarpetas:

#### img/
Almacena imágenes y gráficos generados en el proceso de análisis o despliegue.
Archivos Clave:

#### Hawaii_predicciones.csv

Archivo con las predicciones finales realizadas sobre la muestra de datos de Hawaii.
#### Sintetica.csv

Muestra de datos sintéticos creada para pruebas y análisis.
#### analisis_sentimientos.py

Script en Python que realiza análisis de sentimientos en textos relacionados con los datos.
#### app.py

Script principal que despliega una aplicación interactiva utilizando Streamlit.
#### mapa.py

Genera un mapa de predicción visualizando el éxito de negocios según el modelo.
#### modelo_hawaii.pkl

Archivo serializado que contiene el modelo entrenado para realizar predicciones.
presentacion.py

Script para generar una presentación automática con los resultados del análisis.
#### requirements.txt

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

### Objetivo de la Rama
El propósito principal de esta rama es:

Realizar un análisis exploratorio y limpieza sobre datos de negocios de Hawaii.
Desarrollar un modelo de Machine Learning para predecir el éxito de un negocio.
Crear un despliegue interactivo de la solución usando Streamlit.
Proporcionar recursos adicionales como análisis de sentimientos y visualizaciones.


### Colaboradores:

#### Sergio Castro: Limpieza y análisis del dataset Google.
#### Diana Moreno: Limpieza y análisis del dataset Yelp.
#### Felipe Dedes : Machine learning y despliegue.
#### Greta Combold: Machine Learning y despliegue.
