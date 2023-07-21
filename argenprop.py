import requests

def obtener_propiedades():
    url = "https://api.argenprop.com/api/v1/properties"
    parametros = {
        "operation_types": "sale",
        "property_types": "apartment",
        "zone_ids": "1",
        "sort": "price_desc",
        "limit": 10
    }
    
    headers = {
        "Authorization": "Bearer tu_token_de_acceso"
    }
    
    respuesta = requests.get(url, params=parametros, headers=headers)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        # Aquí puedes procesar los datos de respuesta como desees
        print(datos)
    else:
        print("Error al obtener propiedades:", respuesta.status_code)

# Llamar a la función para obtener propiedades
obtener_propiedades()


if __name__ == '__main__':
    obtener_propiedades()