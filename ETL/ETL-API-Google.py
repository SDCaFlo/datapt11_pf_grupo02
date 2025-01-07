import pandas as pd
import requests
from google.cloud import bigquery
import functions_framework
import json

API_KEY = "AIzaSyCB3vmEcBfzXgwg-Gsliz6itF5UWnx2T1w"
url = "https://places.googleapis.com/v1/places:searchNearby"



def API_load(request):
    request_json = request.get_json()

    latitude = request_json.get("latitude")
    longitude = request_json.get("longitude")

    # Validar que las variables estén presentes
    if not latitude or not longitude:
        return {
            "status": "error",
            "message": "Missing parameters: latitude/longitude required."
        }, 400
    
    
    # definimos el payload de la solicitud.
    payload = {
    "includedPrimaryTypes": ["coffee_shop", "cafe", "cat_cafe", "dog_cafe"],
    "maxResultCount": 20,
    "languageCode": "en",
    "rankPreference": "DISTANCE",
    "locationRestriction": {
        "circle": {
            "center": {
                "latitude": latitude,
                "longitude": longitude
            },
            "radius": 50000.0
        }
    }
    }

    # definimos los headers
    headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask": "places.displayName,places.addressComponents,places.id,places.formattedAddress,places.primaryTypeDisplayName,places.location,places.types,places.rating,places.userRatingCount,places.reviews"
    }

    # se realiza la solicitud
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        data_dict = response.json()
        df = pd.DataFrame(data=data_dict['places'])

        # Aplicamos el tratamiento y guardamos los dataset business y reviews
        business_df, reviews_df, user_df = data_treatment(df)
        
        # Carga a BigQuery
        client = bigquery.Client()
        table_1 = "bamboo-zone-445202-a3.Datanova_CoffeeShops.temp_business_API"
        table_2 = "bamboo-zone-445202-a3.Datanova_CoffeeShops.temp_reviews_API"
        table_3 = "bamboo-zone-445202-a3.Datanova_CoffeeShops.temp_user_API"

        job = client.load_table_from_dataframe(
            business_df,
            table_1,
            job_config=bigquery.LoadJobConfig(
                write_disposition="WRITE_TRUNCATE",
                autodetect=False
            )
        )

        job = client.load_table_from_dataframe(
            reviews_df, 
            table_2,
            job_config=bigquery.LoadJobConfig(
                write_disposition="WRITE_TRUNCATE",
                autodetect=False 
            )
        )

        job = client.load_table_from_dataframe(
        user_df, 
        table_3,
        job_config=bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE",
            autodetect=False 
            )
        )


        return {
            "status": "success",
        }, 200




    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500

def data_treatment(df):
    """Treatment for extracted df"""
    # Extraemos latitude y longitude, dropeamos location.
    df['latitude'] = df['location'].apply(lambda loc: loc['latitude'])
    df['longitude'] = df['location'].apply(lambda loc: loc['longitude'])
    df.drop(columns=['location'], inplace=True)

    # Extramos 'name' de 'displayName'
    df['name'] = df['displayName'].apply(lambda name: name['text'])
    df.drop(columns=['displayName'], inplace=True)

    # Extraemos primary type
    df['primaryType'] = df['primaryTypeDisplayName'].apply(lambda name: name['text'])
    df.drop(columns=['primaryTypeDisplayName'], inplace=True)

    # Tratamiento de la columna addressComponents para obtener ciudad y estado.
    df_test = df[['id','addressComponents']].explode('addressComponents', ignore_index=True)
    address_comp_df = pd.concat([df_test, pd.json_normalize(df_test['addressComponents'])], axis=1)[['id', 'longText','types']]
    address_comp_df['types'] = address_comp_df['types'].astype(str)
    pivot_address_comp_df = address_comp_df.pivot(index='id', columns='types', values='longText').reset_index()
    business_df = pd.merge(df, pivot_address_comp_df[['id', "['administrative_area_level_1', 'political']", "['locality', 'political']"]], on='id')

    # TABLA Business
    business_df.drop(columns=['types', 'addressComponents', 'reviews'], inplace=True)

    # renamer
    business_renamer = {'id': 'business_id',
                    'formattedAddress': 'address',
                    'rating': 'business_star',
                    'userRatingCount':'review_count',
                    'primaryType': 'categories',
                    "['administrative_area_level_1', 'political']": 'state',
                    "['locality', 'political']": 'city'}

    
                    
    business_df.rename(columns=business_renamer, inplace=True)
    business_df['categories'] = business_df['categories'].apply(lambda row: [row,])
    business_df['app_source'] = 'Google'

    #TABLA reviews
    reviews_df = df[['id', 'reviews']]
    reviews_df.dropna(inplace=True) # dropeamos reviews nulos.
    reviews_df = reviews_df.explode('reviews', ignore_index=True) # examinamos los reviews recientes.

    # elegimos las columnas relevantes.
    normalized_reviews = pd.json_normalize(reviews_df['reviews'])[['name', 'rating', 'publishTime', 'originalText.text', 'authorAttribution.displayName', 'authorAttribution.uri']]
    # Despues de normalizar, concatenamos.
    reviews_df_normalized = pd.concat([reviews_df, normalized_reviews], axis=1)
    reviews_df_normalized.drop(columns='reviews', inplace=True)
    # Modificamos la columna fecha.
    reviews_df_normalized['publishTime'] = pd.to_datetime(reviews_df_normalized['publishTime'], format='%Y-%m-%dT%H:%M:%S.%fZ').dt.strftime('%Y-%m-%d %H:%M:%S')
    reviews_df_normalized['publishTime'] = pd.to_datetime(reviews_df_normalized['publishTime'])

    # Extraemos el ID del comentario
    reviews_df_normalized['review_id'] = reviews_df_normalized['name'].apply(str.split,args=('/',)).apply(lambda x: x[1] + '-' + x[3])
    # Extraemos el ID del user
    reviews_df_normalized['user_id'] = reviews_df_normalized['authorAttribution.uri'].apply(str.split,args=('/',)).apply(lambda x: x[5])
    # Removemos columnas innecesarias
    reviews_df_normalized.drop(columns=['name','authorAttribution.uri'], inplace=True)
    # Agregamos el campo app_source
    reviews_df_normalized['app_source']='Google'

    #Apartamos el user_df para actualizar users
    user_df = reviews_df_normalized[['review_id', 'authorAttribution.displayName', 'user_id', 'rating']]
    user_df['app_source'] = 'Google'

    
    reviews_renamer = {'id' : 'business_id',
                    'rating': 'stars',
                    'publishTime': 'date',
                    'originalText.text':'text',
                    'authorAttribution.displayName': 'user_name'
                    }
    reviews_df_normalized.rename(columns=reviews_renamer,inplace=True)

    reviews_df_normalized.drop(columns='user_name', inplace=True)

    user_renamer = {
        'rating': 'stars',
        'authorAttribution.displayName': 'user_name'
    }
    user_df.rename(columns=user_renamer,inplace=True)

    return business_df, reviews_df_normalized, user_df