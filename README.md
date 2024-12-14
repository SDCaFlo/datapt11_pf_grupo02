### <p align="center">  ☕Proyecto: </p>
# <p align="center"> 📊 Análisis de Inversión </p>
## <p align="center"> 🥐 Coffee & Brunch Bussiness </p>

## 📚Índice
 
| Sección                         | Enlace                           |
|--------------------------------|----------------------------------|
| **Items que tiene que tener la propuesta**          | [Equipo de trabajo](#equipo-de-trabajo) |
|                                | [Entendimiento de la situación actual](#entendimiento-de-la-situación-actual) |
|                                | [Objetivos](#objetivos)          |
|                                | [Alcance](#alcance)              |
|                   | [KPIs](#kpis)                    |
|          | [Repositorio Github](#repositorio-github) |
| **Hitos**                      |                                  |
|                         | [3KPIs](#kpis)                   |
| | [Alcance](#alcance)              |
|              | [EDA de los datos](#stack-tecnológico) |
|             | [Repositorio Github](#repositorio-github) |
|             | [Stack Tecnológico](#stack-tecnológico) |
|          | [Metodología de trabajo](#metodología-de-trabajo) |
|                | [Diseño detallado](#diseño-detallado) |
|        | [Cronograma general Gantt](#cronograma-general-gantt) |
| | [Análisis preliminar de calidad de datos](#análisis-preliminar-de-calidad-de-datos) |
| **Documentación:**                      |                                  |
|                                |     [Stack elegido y fundamentación](#Cronograma-general-Gantt)|
|                                |    [Flujo de trabajo](#Flujo-de-trabajo)|
 
---



# Equipo de Trabajo:

Presentación de Nuestro Equipo de Ciencia de Datos
| 📊 **Analistas de Datos** | 🛠️ **Ingenieros de Datos** | 🤖 **Ingenieros de Machine Learning** |
|---------------------------|---------------------------|--------------------------------------|
| ![Claudia y Saray](https://github.com/user-attachments/assets/e24182ce-f116-407d-85f6-e28b149b2f52) | ![Diana y Sergio](https://github.com/user-attachments/assets/c779c3d7-47bb-4c0a-9942-5d8d327701ee) | ![Felipe y Greta](https://github.com/user-attachments/assets/e56af139-909e-48d6-be6b-0313307f840b) |
| **Claudia Jara y Saray Pacheco** <br> Expertas en explorar, interpretar y visualizar los datos, Claudia y Saray son clave para descubrir patrones, generar insights estratégicos y presentar información clara que facilita la toma de decisiones. | **Diana Moreno y Sergio Castro** <br> Diana y Sergio se especializan en diseñar y mantener la infraestructura de datos, asegurando que la información sea accesible, eficiente y escalable para proyectos de alta complejidad. | **Felipe Dedes y Greta Combold** <br> Felipe y Greta lideran el desarrollo de modelos predictivos e implementan soluciones de machine learning que automatizan procesos y generan sistemas inteligentes con impacto real. |

## Juntos, combinamos nuestras habilidades para transformar datos en valor, aportando innovación y resultados efectivos.
***

[⬆️ Volver al índice](#índice)

*** 

![image](https://github.com/user-attachments/assets/90ce882b-4b85-495b-b972-8d3883f69bfa)
¨
# 🔍📊Entendimiento de la situación actual
_"El mercado de cafeterías boutique y brunch está en pleno auge. La creciente demanda por experiencias gastronómicas únicas y la búsqueda de ambientes acogedores lo convierten en un sector atractivo, pero también competitivo.
Sin embargo, los principales desafíos para la expansión incluyen:

1- Identificar zonas con alta demanda potencial.

2- Evaluar la rentabilidad proyectada en cada ubicación.

3- Reducir riesgos asociados a la competencia y baja afluencia de público.

A partir de estos puntos clave, hemos diseñado un análisis que responde directamente a estas inquietudes y ofrece una guía estratégica basada en datos."_

[⬆️ Volver al índice](#índice)

# 🎯✨Objetivos 
![image](https://github.com/user-attachments/assets/75522d77-760b-42c1-ac4b-d091ab9dc7af)

###### Objetivo Específicos:
1. **Realizar un Análisis Exploratorio de los Datos disponibles en Yelp y Google maps (incluir
aquí la otra fuente de dato si aplica)**
2. **Realizar un ETL que permita integrar datos de diversas fuentes y transformarlos en una
estructura unificada.**
3. **Definir el pipeline**
4. **Realizar el despliegue de datos en nube que facilite la ingesta de datos y alimentar el
modelo de machine learning.**
5. **Desarrollar un modelo de machine learning para predecir las oportunidades de inversión
basadas en los KPIs definidos.**
6. **Elaborar un dashboard de los KPIs e información clave de consulta.**

[⬆️ Volver al índice](#índice)


# 📏🌍Alcance
![image](https://github.com/user-attachments/assets/77078868-bc06-43e7-8441-68e18f3bb3ef)

 
Este proyecto se centra en realizar un análisis integral del mercado para apoyar la expansión estratégica del negocio 'Coffee & Brunch Business'. Consideramos los siguientes puntos clave dentro del alcance:
1. Recopilación y procesamiento de datos provenientes de Yelp, Google Maps y otras fuentes relevantes.
2. Diseño e implementación de un ETL para integrar y estructurar los datos en un formato unificado.
3. Identificación de zonas de alto potencial mediante análisis geoespacial y evaluación de métricas clave.
4. Desarrollo de un modelo predictivo de machine learning para estimar oportunidades de inversión.
5. Creación de un dashboard interactivo para la visualización de KPIs e insights relevantes.
Este alcance está diseñado para ofrecer resultados accionables y maximizar el retorno de inversión, alineándose con los objetivos de crecimiento del negocio.

ALCANCE Este proyecto incluirá el análisis y limpieza de datos disponibles en Yelp y Google Maps para negocios de cofee and breakfast en Estados Unidos, la elaboración de un dashboard interactivo con la visualización de datos claves y Kpi y la implementación de un modelo de machine learning para predicciones y recomendaciones sobre la expansión de este tipo de negocio.
Este proyecto no incluye la Integración en tiempo real con las plataformas Yelp o google maps, análisis de información por fuera de Estados Unidos ni tampoco estrategías de marketing de expansión que se puede desarrollar en una siguiente etapa.

[⬆️ Volver al índice](#índice)
***
![image](https://github.com/user-attachments/assets/ffc4470f-6ecf-4bfc-93a7-85bf48843901)

# 📈🔎 EDA: Análisis Exploratorio de Datos
"En estas dos primeras semanas, nos enfocamos en recopilar, limpiar y analizar datos de Google Maps y Yelp. Nuestro EDA inicial incluye:
Demografía y densidad poblacional: Identificar zonas con alta concentración de población objetivo.
Tráfico peatonal: Evaluar la afluencia promedio en las áreas seleccionadas.
Competencia: Mapear la presencia de negocios similares.
Presentaremos gráficos claros que reflejen tanto los datos generales como los resultados después de la limpieza. Por ejemplo, visualizaremos las áreas con mayor potencial versus las que presentan riesgos asociados a la saturación del mercado."
![image](https://github.com/user-attachments/assets/ed9d7354-6ee9-415d-9fe0-f09b934d5852)
Para la base de datos de YELP encontramos alrededor de 150 mil comercios, los cuales se encuentran ubicados en 1416 ciudades de estados unidos, y como nos muestra el primer gráfico se encuentran mayormente concentrados en la ciudad de philadelphia con un 9.7%, Tucson con un 6.15% y tampa con un 6%.
Como el negocio objetivo del cliente son los negocios dedicados al comercio de Coffee & Tea y Breakfast and brunch, el segundo gráfico nos muestra la cantidad de negocios en estas categorías.Para este caso contamos con 11.758 negocios de estas categorías ubicados en un total de 616 ciudades de Estados Unidos, y como podemos observar, la mayor parte de estos negocios los podemos encontrar, en philadelphia, tampa, new Orleans, Tucson y Nashville. Siento Philadelphia la ciudad con más negocios de este tipo en Estados Unidos.

![image](https://github.com/user-attachments/assets/d1505e48-0341-4e81-9717-a33843231fc7)
En los datos de YELP también encontramos un poco más de 7 millones de reseñas escritas por los usuarios, de las cuales 1.147.000 corresponden a reseñas de la categoría Coffee and Breakfast.
En el gráfico de color azul, podemos ver la concentración de estas reseñas por ciudades, mostrando que en Philadelphia y New Orleans se encuentran la mayor cantidad de reseñas del todo el dataset.

Y, por último, tenemos un gráfico que nos muestra la cantidad de usuarios que han dejado reseñas en este tipo de comercios. 
Tenemos 574.000 usuarios con reseñas en las 616 ciudades, mostrando la mayor concentración de estos en Philadelphia, seguido por Tampa, New Orleans e Indianapolis.
Mostrando a Philadelphia como un gran destino para este tipo de negocios.

![image](https://github.com/user-attachments/assets/29ff9ab1-5e8d-4b39-b0a1-a97a406a9053)
![image](https://github.com/user-attachments/assets/f80f2792-daf3-4045-b0ee-c53144117cce)
Para el dataset de google se analizaron un total 2,9 millones de negocios y 89.9 millones de reviews para el periodo de tiempo que conlleva desde abril-2002 hasta septiembre-2021.
Se identificaron un total de 4461 categorías distintas, de las cuales se tomaron las 50 categorías de comida más relevantes, que representan más del 90% de los reviews totales asociados a establecimientos de comida.

Wordcloud: Se extrajo las palabras con mayor aparición dentro de las 50 categorías top y se produjo el siguiente wordcloud. Aquí logramos identificar que las palabras más relevantes son:  "fast," "food", "takeout”, “pizza”, “coffee”, ‘cafe’.

Rating Medio Categorías: Teniendo en cuenta esto, calculamos el rating promedio de las categorías y observamos que los establecimientos asociados a Coffee presentan un rating mucho más elevado, en contraste con los locales de comida rápida, que se encuentran entre los peores calificados.

Establecimientos Unicos por Periodo: Despues de acotar nuestro locales a categorias asociadas a Coffee shops, evaluamos la presencia de establecimientos dentro de los reviews con una frecuencia trimestral. De esta manera, observamos que el sector se encuentra en crecimiento, a excepción de un periodo de decaída posiblemente asociado a la pandemia.

Rating promedio por periodo: A pesar de esta caída, notamos que el rating promedio de estos establecimientos ha ido en alza, lo que puede ser un indicador tanto de una mejora constante en el servicio debido a la competencia del sector, así como también una mejor aceptación del público a este tipo de establecimientos.


Conclusión: "Coffee" y "shop" son términos destacados, lo que indica la popularidad de cafeterías y lugares donde los consumidores buscan bebidas rápidas y espacios para socializar o trabajar. Esto es consistente con la cultura estadounidense, donde el café ocupa un lugar central.

[⬆️ Volver al índice](#índice)
***

 # 📊📏KPIs
 ![image](https://github.com/user-attachments/assets/4deac3ae-91b7-4b3b-90d1-95bd26fdfcc2)

KPIS
En un mercado competitivo, el crecimiento y la salud de un negocio dependen de decisiones fundamentadas en datos. Por ello, hemos diseñado un sistema de medición basado en indicadores clave de desempeño (KPIs) que nos permitirán rastrear y optimizar aspectos esenciales como la satisfacción del cliente, la visibilidad del negocio y la conversión hacia compras efectivas. Este enfoque, sustentado por tecnología avanzada, buscará garantizar una gestión estratégica y escalable. 
proponer objetivo de crecimiento y cuanto tiempo
KPI1:

Nombre:Tasa de crecimiento de comentarios positivos
Objetivo: Monitorear la satisfacción de los clientes y la salud de la marca.
Métrica: ¿Está creciendo el volumen de opiniones positivas sobre nuestro negocio?
Descripción: mide el porcentaje de crecimiento de la cantidad total de puntuaciones positivas con respecto al periodo inmediatamente anterior
 
Fórmula: % de crecimiento de comentarios positivos = [(Total comentarios positivos periodo actual - Total comentarios positivos periodo anterior) / Total de comentarios positivos periodo anterior] * 100
 
KPI2:
Nombre: Puntuación promedio
Objetivo: Representar de forma cuantitativa la experiencia del cliente.
Métrica: Promedio de calificaciones otorgadas por los usuarios.
Descripción: Mide la satisfacción de los clientes representada por medio de la  puntuación que registran los usuarios para el negocio.

Fórmula: Puntaje promedio = Sumatoria total de los puntajes del periodo / Total usuarios que dejaron su calificación en el periodo.
 
KPI3
Nombre: Tasa de crecimiento de las calificaciones
Objetivo: Incrementar la visibilidad del negocio atrayendo a más clientes a dejar reseñas.
Métrica: ¿Cuánto crecen las reseñas en cada periodo?
Descripción:  Medir el crecimiento de la cantidad de clientes que están dejando reseñas, lo que refleja la visibilidad del negocio.

Fórmula: % de crecimiento de comentarios de las calificaciones = [(Total comentarios periodo actual - Total comentarios periodo anterior) / Total de comentarios periodo anterior] * 100

Puntaje promedio = Sumatoria total de los puntajes del periodo / Total usuarios que dejaron su calificación en el periodo.

[⬆️ Volver al índice](#índice)

## 🛠️💻Stack Tecnológico
![Imagen de WhatsApp 2024-12-12 a las 15 21 29_82e29ee7](https://github.com/user-attachments/assets/b267e89d-98ee-4e1d-936c-bb9f57ccf953)
Para garantizar que estas métricas se capturen, transformen y analicen eficientemente, implementaremos una arquitectura robusta de Data Warehouse y Machine Learning divididas en cuatro módulos, la extracción, transformación, data warehouse y visualización y machine learning
Extracción: 
Se considerará la extracción de datos de diversas fuentes, y se realizará carga de forma local, así como también extracción via web scrapping y APIs de ser necesario. (Por definir).
Transformación:
Cloud Scheduler: Las tareas de extracción se automatizarán utilizando.
Cloud Functions: Programar scripts de transformación simples, que no requieran mucho poder de procesamiento y sean rápidos. Así como también activar los procesos BigQuery y DataFlow.
BigQuery: Se encargará de realizar transformaciones de fuentes de datos de mayor tamaño usando queries SQL.
DataFlow: Se encargará de procesar data que no pueda transformarse usando SQL especialmente la que se usará para el modelo de machine learning

Datawarehouse:
BigQuery: Se usará BigQuery también como almacén de datos. Ventajas: Se evita cargar datos desde google cloud storage e incurrir en gastos de transferencia. Data lista para ser procesada por otras herramientas después del ETL.

Visualización y ML
Streamlit: Se hará uso de streamlit para generar un dashboard interactivo, así como también para realizar el deploy del modelo de ML.
Una vez diseñada la app de streamlit, esta se conteinerizará con Docker para que pueda ser deployada en la nube de GCloud.
Se hará uso de tecnologías de cloud como, Cloud Container Registry, y Cloud Run para poder guardar y deployar el container.

[⬆️ Volver al índice](#índice)

# Flujo de Trabajo
# Pipeline 

## 📝🧩 Metodología de trabajo
![image](https://github.com/user-attachments/assets/06a7dbf2-a68d-4d93-9506-f11b931324e6)

"Para organizar nuestro trabajo y dirigir nuestros esfuerzos hacia nuestras metas, hemos elegido trabajar con metodologías ágiles bajo el marco de trabajo SCRUM. Este enfoque nos va a permitir mejorar la organización de tareas, fomentar la colaboración entre los integrantes del equipo y adaptarnos rápidamente a los cambios, asegurando entregas continuas y alineadas con nuestros objetivos."
[⬆️ Volver al índice](#índice)

## ⏳📅Cronograma General Gantt
![image](https://github.com/user-attachments/assets/168deebf-1e27-404d-83bc-728ebc353a4b)

Cronograma General: Hitos y Entregables
"El proyecto está diseñado para ser entregado en seis semanas, con presentaciones cada dos semanas.
Semana 1-2:
EDA inicial con datos de Google Maps y Yelp.
Gráficos que muestren la información limpia y general.
Definición de KPIs y fórmulas, junto con las metas iniciales.
Semana 3-4:
Implementación de un modelo predictivo para analizar la rentabilidad de las zonas priorizadas.
Mapas interactivos que representen el análisis geoespacial.
Semana 5-6:
Finalización del dashboard interactivo.
Presentación de recomendaciones finales y conclusiones basadas en los KPIs.
Hitos:
Desarrollo de herramientas visuales.
Documentación clara del análisis.
Recomendaciones estratégicas accionables."

![gantt](https://github.com/user-attachments/assets/e9c25815-c014-4e27-86af-31defa961134)

El cronograma general del proyecto se detalla a continuación, dividido en secciones como inicio, análisis, desarrollo y finalización. Utilizamos un diagrama de Gantt para visualizar el progreso de cada tarea.

```mermaid
gantt
    title Cronograma General del Proyecto
    dateFormat  YYYY-MM-DD
    section Sprint 1
    Contextualizar la problemática    :done, b1, 2024-12-02, 2d
    Definiciones de objetivos y alcance  :done, a2, 2024-12-04, 1d
    Comprender los datos disponibles  :done, a2, 2024-12-04, 2d
    Definición de Stack Tecnológico  :done, a2, 2024-12-05, 3d
    EDA y ETL inicial  :done, a2, 2024-12-05, 6d
    Definición y KPIs  :done, a2, 2024-12-10, 3d
    Preparación y ensayo de presentación :done, a2, 2024-12-10, 4d
    section Sprint 2 
    ETL completo      :active, b1, 2024-12-06, 5d
    Pipeline y automatización            :b2, 2024-12-11, 3d
    Diseño del Datawarehouse          :b2, 2024-12-11, 3d
    Diseño del modelo ER          :b2, 2024-12-11, 3d
    MVP Machine Learning         :b2, 2024-12-11, 3d
    Documentación        :b2, 2024-12-11, 3d
    Preparación y Ensayo   :b2, 2024-12-11, 3d
    section Sprint 3 
    Diseño de Reportes/Dashboards           :c1, 2024-12-14, 7d
    KPIs                  :c2, 2024-12-21, 4d
    Modelo de Machine Learning  :c2, 2024-12-21, 4d
    Documentación               :d1, 2024-12-25, 3d
    Preparación y ensayo de presentación       :d2, 2024-12-28, 1d
```
[⬆️ Volver al índice](#índice)

# 🔗📂Repositorio Github
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

[⬆️ Volver al índice](#índice)

***
"Estamos convencidos de que este proyecto será el punto de partida para la expansión exitosa de su negocio. Nuestro trabajo no solo busca identificar ubicaciones rentables, sino también brindarle herramientas que faciliten decisiones basadas en datos sólidos y confiables.
Hoy le presentamos los primeros resultados de este proceso. A medida que avancemos, le mostraremos más hallazgos, siempre con la misión de maximizar su éxito en este sector tan competitivo."

### Contacto:
#### Claudia Jara Yañez:
Rol: Data Analyst
Github:https://github.com/claujara1975

Linkedin:

#### Saray Pacheco Ramos:
Rol: Data Analyst  
Github: https://github.com/ssaraypr

#### Sergio Castro: Limpieza y análisis del dataset Google.
Rol: Data Engineer
Github:https://github.com/SDCaFlo

LinkedIn: 
#### Diana Moreno: Limpieza y análisis del dataset Yelp.
Rol:  Data Engineer
Github: https://github.com/dianitafeliz

LinkedIn:
#### Felipe Dedes : Machine learning y despliegue.
Rol: Machine Learning Engineer
Github:https://github.com/DedesF

LinkedIn:
#### Greta Combold: Machine Learning y despliegue.
Rol: Machine Learning Engineer
Github: https://github.com/PerlaMarGreta

LinkedIn:

[⬆️ Volver al índice](#índice)
